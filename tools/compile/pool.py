"""The models the compiler can call, chosen by role and by what quota each has left.

Every provider speaks the OpenAI chat API. A role (vision, strong, fast) lists models from both providers in order of
preference; a call goes to the next model of the role that is not exhausted and not busy, and a model whose free
quota runs out is set aside for the rest of the run (and remembered in the ledger). Thinking is switched off unless the
task asks for it: most steps are transcription, where hidden reasoning only spends quota (and, under a token cap, can
leave no room for the answer).
"""
from __future__ import annotations

import base64
import json
import os
import re
import threading
import time
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path

from .store import LEDGER

PROVIDERS = {
    "qianwen": ("https://maas.qianwenaiapi.com/compatible-mode/v1", "QIANWEN_API_KEY"),
    "tokenhub": ("https://tokenhub.tencentmaas.com/v1", "TENCENT_TOKENHUB_KEY"),
}

ROLES: dict[str, list[str]] = {
    # looks at one small picture and says what it is
    "vision": ["qianwen:qwen3-vl-plus", "qianwen:qwen3.5-omni-plus", "qianwen:qwen3.8-omni-flash",
               "tokenhub:hy-vision-2.0-instruct", "tokenhub:deepseek/deepseek-v4-flash-vision-exp", "tokenhub:hy4"],
    # solves questions, builds outlines, writes and checks explanations (diverse families, think=False fast path)
    "strong": ["qianwen:qwen3.8-max", "tokenhub:deepseek-v4-pro-202606", "qianwen:qwen3.8-max-0902",
               "tokenhub:kimi-k3.1-pro-highspeed", "qianwen:qwen3.7-max", "tokenhub:deepseek-v4-pro-0813",
               "qianwen:qwen3.7-max-2026-06-08", "tokenhub:minimax-m3", "qianwen:deepseek-v4-pro-0813",
               "tokenhub:kimi-k3.1-pro", "qianwen:qwen3.7-plus", "tokenhub:hy4-preview",
               "qianwen:deepseek-v4-pro", "tokenhub:deepseek-v4-pro", "qianwen:qwen3.6-plus",
               "tokenhub:kimi-k2.8-preview", "tokenhub:mimo-v2.6-pro", "tokenhub:kimi-k3"],
    # classifies and tidies
    "fast": ["qianwen:qwen3.6-flash", "qianwen:qwen3.7-flash", "qianwen:deepseek-v4.1-flash",
             "qianwen:qwen3.8-flash", "qianwen:qwen3.8-27b", "tokenhub:deepseek-v4.1-flash",
             "tokenhub:deepseek-v4-flash-202605", "qianwen:deepseek-v4.1-flash-1017",
             "qianwen:qwen3.5-flash", "tokenhub:deepseek-v4.1-flash-1017", "tokenhub:mimo-v2.6-flash"],
}
PER_MODEL = 6          # calls in flight per model
QUOTA_WORDS = re.compile(r"quota|额度|insufficient|balance|欠费|Arrearage|limit.*exceed|free.*(used|exhaust)", re.I)


@dataclass
class Model:
    provider: str
    name: str
    gate: threading.Semaphore = field(default_factory=lambda: threading.Semaphore(PER_MODEL))
    cooldown_until: float = 0.0

    @property
    def id(self) -> str:
        return f"{self.provider}:{self.name}"


class Exhausted(Exception):
    pass


class Stalled(Exception):
    pass


QUIET = 30        # seconds a model may send nothing (not even reasoning) before the call goes to another model
LONGEST = 150     # seconds a whole answer may take


def _streamed(request: urllib.request.Request) -> tuple[str, dict | None]:
    """The answer of a streamed call and its usage. Streaming shows a call is alive token by token, so a model that
    has hung is noticed in QUIET seconds instead of after a whole-answer timeout."""
    started = time.monotonic()
    parts: list[str] = []
    usage = None
    with urllib.request.urlopen(request, timeout=QUIET) as response:
        for raw in response:
            if time.monotonic() - started > LONGEST:
                raise Stalled("answer took too long")
            line = raw.decode("utf-8", "replace").strip()
            if not line.startswith("data:"):
                continue
            data = line[5:].strip()
            if data == "[DONE]":
                break
            chunk = json.loads(data)
            usage = chunk.get("usage") or usage
            for choice in chunk.get("choices") or []:
                parts.append((choice.get("delta") or {}).get("content") or "")
    return "".join(parts), usage


class Pool:
    def __init__(self) -> None:
        self.lock = threading.Lock()
        try:
            self.ledger = json.loads(LEDGER.read_text(encoding="utf-8")) if LEDGER.exists() else {}
        except (OSError, json.JSONDecodeError):
            self.ledger = {}
        self.models = {spec: Model(*spec.split(":", 1)) for specs in ROLES.values() for spec in specs}
        self.turn = {role: 0 for role in ROLES}

    def _save(self) -> None:
        LEDGER.parent.mkdir(parents=True, exist_ok=True)
        tmp = LEDGER.with_name(f"{LEDGER.name}.{os.getpid()}.{threading.get_ident()}.tmp")
        try:
            tmp.write_text(json.dumps(self.ledger, ensure_ascii=False, indent=1), encoding="utf-8")
            os.replace(tmp, LEDGER)
        except OSError:
            tmp.unlink(missing_ok=True)

    def _usable(self, spec: str) -> bool:
        m = self.models[spec]
        return bool(os.environ.get(PROVIDERS[m.provider][1])) and not self.ledger.get(spec, {}).get("exhausted")

    def _pick(self, role: str, avoid: str | None) -> Model:
        """The next usable model of the role, waiting while all are busy."""
        while True:
            now = time.monotonic()
            with self.lock:
                specs = [s for s in ROLES[role] if self._usable(s) and (avoid is None or not s.startswith(avoid))]
                if not specs:
                    specs = [s for s in ROLES[role] if self._usable(s)]
                if not specs:
                    raise Exhausted(f"every {role} model has used up its quota")
                ready = [s for s in specs if now >= self.models[s].cooldown_until] or specs
                for offset in range(len(ready)):
                    model = self.models[ready[(self.turn[role] + offset) % len(ready)]]
                    if model.gate.acquire(blocking=False):
                        self.turn[role] = (self.turn[role] + offset + 1) % len(ready)
                        return model
            time.sleep(0.3)

    def _record(self, model: Model, usage: dict | None, exhausted: str | None = None) -> None:
        with self.lock:
            entry = self.ledger.setdefault(model.id, {"tokens": 0, "calls": 0})
            if usage:
                entry["tokens"] += int(usage.get("total_tokens") or 0)
                entry["calls"] += 1
            if exhausted:
                entry["exhausted"] = exhausted[:200]
            self._save()

    def chat(self, role: str, messages: list[dict], *, think: bool = False, max_tokens: int = 8000,
             avoid: str | None = None) -> tuple[str, str]:
        """(answer, model id). `avoid` names a provider to stay away from, so a check is made by another family."""
        # A thinking model spends its reasoning out of the same budget: give it room, or the answer comes back empty.
        for attempt in range(12):
            model = self._pick(role, avoid)
            base, key_name = PROVIDERS[model.provider]
            budget = max(max_tokens, 16000) if think or (model.provider == "tokenhub" and model.name.startswith("glm")) else max_tokens
            body = {"model": model.name, "messages": messages, "max_tokens": budget, "stream": True,
                    "stream_options": {"include_usage": True}}
            # Qianwen takes enable_thinking; TokenHub's models take thinking.type, except GLM, which always thinks
            # and so only serves steps that want thinking.
            if model.provider == "qianwen":
                body["enable_thinking"] = think
            elif not think and not model.name.startswith("glm"):
                body["thinking"] = {"type": "disabled"}
            request = urllib.request.Request(f"{base}/chat/completions", data=json.dumps(body).encode(),
                                             headers={"Authorization": f"Bearer {os.environ[key_name]}",
                                                      "Content-Type": "application/json"})
            wait = 0.0
            try:
                content, usage = _streamed(request)
                self._record(model, usage)
                if content.strip():
                    return content, model.id
                model.cooldown_until = time.monotonic() + 10
            except urllib.error.HTTPError as error:
                detail = error.read().decode("utf-8", "replace")
                if QUOTA_WORDS.search(detail) or error.code in (402,):
                    self._record(model, None, exhausted=detail)
                elif error.code in (400, 403, 404) and re.search(r"model|不支持|not activated|access denied", detail, re.I):
                    self._record(model, None, exhausted=f"unavailable: {detail}")
                else:
                    model.cooldown_until = time.monotonic() + (20 if error.code == 429 else 10)
                    wait = min(15, 1.5 * (attempt + 1))
            except (urllib.error.URLError, TimeoutError, ConnectionError, Stalled):
                model.cooldown_until = time.monotonic() + 20
                wait = min(15, 1.5 * (attempt + 1))
            finally:
                model.gate.release()
            if wait:
                time.sleep(wait)
        raise RuntimeError(f"{role} call failed after retries")


def image_part(path: Path) -> dict:
    kind = "png" if path.suffix.lower() == ".png" else "jpeg"
    return {"type": "image_url", "image_url": {"url": f"data:image/{kind};base64,{base64.b64encode(path.read_bytes()).decode()}"}}


def json_of(text: str):
    """The JSON value in a model's answer, fenced or not."""
    fenced = re.search(r"```(?:json)?\s*(.+?)```", text, re.S)
    raw = fenced.group(1) if fenced else text
    starts = [i for i in (raw.find("{"), raw.find("[")) if i >= 0]
    if not starts:
        raise ValueError(f"no JSON in answer: {text[:120]!r}")
    start = min(starts)
    end = max(raw.rfind("}"), raw.rfind("]")) + 1
    try:
        return json.loads(raw[start:end], strict=False)
    except json.JSONDecodeError as error:
        raise ValueError(f"bad JSON: {error}") from error
