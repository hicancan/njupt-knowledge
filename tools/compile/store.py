"""Where the compiler keeps what it has made outside the repository: page images, parses, every model answer.

Everything is keyed by what it was made from (the content's hash, the step and the step's version), so a run that is
stopped resumes where it was, a page is never paid for twice, and changing one step's version redoes only that step.
"""
from __future__ import annotations

import hashlib
import json
import os
import threading
from pathlib import Path
from typing import Callable

WORK = Path(r"D:\Data\njupt-knowledge-sources")
CACHE = WORK / "cache"
PAGES = WORK / "pages"
LEDGER = WORK / "ledger.json"


def key(*parts: object) -> str:
    return hashlib.sha256("\x1f".join(str(part) for part in parts).encode("utf-8")).hexdigest()[:32]


def cached(step: str, version: int, parts: tuple, make: Callable[[], object]):
    """make()'s result, from the cache when the same step at the same version has seen the same parts."""
    path = CACHE / step / f"{key(version, *parts)}.json"
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    value = make()
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(f"{path.name}.{os.getpid()}.{threading.get_ident()}.tmp")
    tmp.write_text(json.dumps(value, ensure_ascii=False), encoding="utf-8")
    os.replace(tmp, path)
    return value
