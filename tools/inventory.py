"""Stage 0: know what a source holds before compiling any of it.

    python tools/inventory.py <source id> <folder> [--taught <information.json>]

Every file under the folder (archives unpacked beside a working copy, never in the folder itself) gets one line in
sources/<source id>.jsonl: its path, size and content hash, the course it belongs to, what kind of document it is,
and which earlier line it duplicates. Nothing is parsed or rewritten here; the next
stages read this list.

    kind     期末试卷 / 答案 / 复习要点 / 习题 / 课件 / 实验 / 教材 / 竞赛论文 / 软件 / 其他
    course   a course plan's code when the folder names a course taught now (by name or nickname), else null
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORK = Path(r"D:\Data\njupt-knowledge-sources\unpacked")
SEVEN_ZIP = r"C:\Program Files\7-Zip\7z.exe"
ARCHIVES = {".zip", ".rar", ".7z"}
SKIP = {".pyc", ".ds_store", ".gitattributes", ".gitignore"}

KINDS = [  # first match wins; tested against the path below the source root
    ("软件", r"软件|\.exe$|\.msi$|安装包|编译器"),
    ("竞赛论文", r"美赛|数学建模竞赛|O奖|特等奖|论文集"),
    ("教材", r"大话|第\s*\d+\s*版|教材(?!.*(习题|答案))|教程(?!.*(习题|答案))|电子书|原著"),
    ("答案", r"答案|解答|题解|参考解|活页答案"),
    ("期末试卷", r"期末|期中|真题|试卷|[A-D]卷|考题|样题|题库|模拟题"),
    ("复习要点", r"复习|要点|提纲|大纲|重点|总结|笔记"),
    ("习题", r"习题|作业|练习|题目"),
    ("实验", r"实验|报告|lab"),
    ("课件", r"课件|ppt|讲义|chapter|第.{1,3}章|\.pptx?$"),
]
BOOK_BYTES = 40 * 1024 * 1024  # a single PDF this large is a scanned book, not a paper


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def unpack(archive: Path, into: Path) -> None:
    if into.exists():
        return
    into.mkdir(parents=True)
    result = subprocess.run([SEVEN_ZIP, "x", "-y", f"-o{into}", str(archive)], capture_output=True)
    if result.returncode != 0:
        shutil.rmtree(into)
        raise RuntimeError(f"could not unpack {archive}")


def files(source: str, folder: Path):
    """Every file with its path as listed (archives contribute their members as archive/member)."""
    for path in sorted(folder.rglob("*")):
        if not path.is_file() or path.suffix.lower() in SKIP or ".git" in path.parts:
            continue
        rel = path.relative_to(folder).as_posix()
        if path.suffix.lower() in ARCHIVES:
            into = WORK / source / rel
            try:
                unpack(path, into)
            except RuntimeError as error:
                yield rel, path, str(error)
                continue
            for member in sorted(into.rglob("*")):
                if member.is_file() and member.suffix.lower() not in SKIP:
                    yield f"{rel}/{member.relative_to(into).as_posix()}", member, None
            continue
        yield rel, path, None


def taught_courses(information: Path, nicknames: Path | None) -> list[tuple[str, str]]:
    """(name, code) for every course plan taught now, plus every nickname of it, longest names first."""
    items = json.loads(information.read_text(encoding="utf-8"))["items"]
    pairs = []
    for item in items:
        if item.get("subtype") != "information:course-plan":
            continue
        code = item["id"].rsplit("/", 1)[1]
        for name in [*item["names"], *item.get("aliases", [])]:
            plain = re.sub(r"[（(].*?[)）]|\s", "", name)
            if len(plain) >= 2:
                pairs.append((plain, code))
    return sorted(set(pairs), key=lambda pair: -len(pair[0]))


def course_of(rel: str, courses: list[tuple[str, str]]) -> str | None:
    """The course a path names: the folder nearest the top that matches a taught course's name."""
    for part in rel.split("/")[:-1] or [rel]:
        plain = re.sub(r"【[^】]*】|[（(].*?[)）]|\s|\d+$", "", part)
        code = re.match(r"【([A-Z0-9]+)】", part)
        if code:
            return code.group(1)
        for name, course in courses:
            if plain == name or (len(name) >= 3 and plain.startswith(name)):
                return course
    return None


def kind_of(rel: str, size: int) -> str:
    for kind, pattern in KINDS:
        if re.search(pattern, rel, re.I):
            if kind == "课件" and rel.lower().endswith(".pdf") and size >= BOOK_BYTES:
                return "教材"
            return kind
    return "教材" if rel.lower().endswith(".pdf") and size >= BOOK_BYTES else "其他"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source")
    parser.add_argument("folder", type=Path)
    parser.add_argument("--taught", type=Path, required=True, help="the data release's entities/information.json")
    args = parser.parse_args()
    courses = taught_courses(args.taught, None)
    seen: dict[str, str] = {}
    for other in sorted((ROOT / "sources").glob("*.jsonl")):
        if other.stem == args.source:
            continue
        for line in other.read_text(encoding="utf-8").splitlines():
            row = json.loads(line)
            seen.setdefault(row["sha256"], f"{other.stem}:{row['path']}")
    rows = []
    for rel, path, error in files(args.source, args.folder):
        if error:
            rows.append({"path": rel, "error": error})
            continue
        digest, size = sha256(path), path.stat().st_size
        kind = kind_of(rel, size)
        row = {"path": rel, "bytes": size, "sha256": digest, "course": course_of(rel, courses), "kind": kind,
               "duplicates": seen.get(digest)}
        seen.setdefault(digest, f"{args.source}:{rel}")
        rows.append(row)
    out = ROOT / "sources" / f"{args.source}.jsonl"
    out.parent.mkdir(exist_ok=True)
    out.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8")
    kinds: dict[str, int] = {}
    for row in rows:
        kinds[row.get("kind", "错误")] = kinds.get(row.get("kind", "错误"), 0) + 1
    unmatched = sum(1 for row in rows if "kind" in row and not row["course"])
    duplicated = sum(1 for row in rows if row.get("duplicates"))
    print(f"{len(rows)} files, {duplicated} duplicates, {unmatched} without a course; kinds {kinds}")


if __name__ == "__main__":
    sys.exit(main())
