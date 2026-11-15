"""The models the compiler can call, chosen by role and by what quota each has left.

Every provider speaks the OpenAI chat API. A role (strong, fast) lists models from both providers in order of
preference; a call goes to the next model of the role that is not exhausted and not busy, and a model whose free
quota runs out is set aside for the rest of the run (and remembered in the ledger). Thinking is switched off unless the
task asks for it: most steps are transcription, where hidden reasoning only spends quota (and, under a token cap, can
leave no room for the answer).
"""
from __future__ import annotations

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
    # solves questions, builds outlines, writes and checks explanations
    "strong": ["qianwen:qwen3.8-max", "tokenhub:deepseek-v4-pro-0813", "qianwen:qwen3.7-max", "tokenhub:glm-5.3",
               "qianwen:deepseek-v4-pro-0813", "tokenhub:kimi-k3.1-pro", "qianwen:glm-5.3"],
    # classifies and tidies
    "fast": ["qianwen:qwen3.7-flash", "tokenhub:deepseek-v4.1-flash", "qianwen:qwen3.7-plus", "qianwen:deepseek-v4.1-flash"],
}
PER_MODEL = 3          # calls in flight per model
QUOTA_WORDS = re.compile(r"quota|额度|insufficient|balance|欠费|Arrearage|limit.*exceed|free.*(used|exhaust)", re.I)


@dataclass
class Model:
    provider: str
    name: str
    gate: threading.Semaphore = field(default_factory=lambda: threading.Semaphore(PER_MODEL))

    @property
    def id(self) -> str:
        return f"{self.provider}:{self.name}"


class Exhausted(Exception):
    pass


class Pool:
    def __init__(self) -> None:
        self.lock = threading.Lock()
        self.ledger = json.loads(LEDGER.read_text(encoding="utf-8")) if LEDGER.exists() else {}
        self.models = {spec: Model(*spec.split(":", 1)) for specs in ROLES.values() for spec in specs}
        self.turn = {role: 0 for role in ROLES}

    def _save(self) -> None:
        LEDGER.parent.mkdir(parents=True, exist_ok=True)
        LEDGER.write_text(json.dumps(self.ledger, ensure_ascii=False, indent=1), encoding="utf-8")

    def _usable(self, spec: str) -> bool:
        return not self.ledger.get(spec, {}).get("exhausted")

    def _pick(self, role: str, avoid: str | None) -> Model:
        """The next usable model of the role, waiting while all are busy."""
        while True:
            with self.lock:
                specs = [s for s in ROLES[role] if self._usable(s) and (avoid is None or not s.startswith(avoid))]
                if not specs:
                    specs = [s for s in ROLES[role] if self._usable(s)]
                if not specs:
                    raise Exhausted(f"every {role} model has used up its quota")
                for offset in range(len(specs)):
                    model = self.models[specs[(self.turn[role] + offset) % len(specs)]]
                    if model.gate.acquire(blocking=False):
                        self.turn[role] = (self.turn[role] + offset + 1) % len(specs)
                        return model
            time.sleep(0.5)

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
        budget = max(max_tokens, 16000) if think or role == "strong" else max_tokens
        for attempt in range(12):
            model = self._pick(role, avoid)
            base, key_name = PROVIDERS[model.provider]
            body = {"model": model.name, "messages": messages, "max_tokens": budget, "stream": False}
            # Qianwen takes enable_thinking; TokenHub's models take thinking.type, except GLM, which always thinks
            # and so only serves steps that want thinking.
            if model.provider == "qianwen":
                body["enable_thinking"] = think
            elif not think and not model.name.startswith("glm"):
                body["thinking"] = {"type": "disabled"}
            request = urllib.request.Request(f"{base}/chat/completions", data=json.dumps(body).encode(),
                                             headers={"Authorization": f"Bearer {os.environ[key_name]}",
                                                      "Content-Type": "application/json"})
            try:
                with urllib.request.urlopen(request, timeout=600) as response:
                    answer = json.load(response)
                self._record(model, answer.get("usage"))
                content = answer["choices"][0]["message"].get("content") or ""
                if content.strip():
                    return content, model.id
            except urllib.error.HTTPError as error:
                detail = error.read().decode("utf-8", "replace")
                if QUOTA_WORDS.search(detail) or error.code in (402,):
                    self._record(model, None, exhausted=detail)
                elif error.code in (400, 404) and ("model" in detail.lower() or "不支持" in detail):
                    self._record(model, None, exhausted=f"unavailable: {detail}")
                else:
                    time.sleep(min(60, 2 ** attempt))
            except (urllib.error.URLError, TimeoutError, ConnectionError):
                time.sleep(min(60, 2 ** attempt))
            finally:
                model.gate.release()
        raise RuntimeError(f"{role} call failed after retries")


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
