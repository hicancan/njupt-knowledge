"""Check every link in the knowledge and write what readers need: build/knowledge.json and the documents beside it.

    courses/<code>.md        a course's outline: chapters in teaching order, each a list of topic links
    topics/<subject>/<t>.md  one topic; `requires:` names the topics it builds on
    materials/<src>/<code>/  one source document made into Markdown, each question under its own heading
                             with a 知识点 line linking the topics it tests

A topic's backlinks (the courses that teach it, the questions that test it, the topics built on it) are computed here,
never written by hand. Any link to something that does not exist stops the build.
"""
from __future__ import annotations

import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "build"
LINK = re.compile(r"\[([^\]]+)\]\(([^)\s]+\.md)(#[^)]*)?\)")
HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*$")


def front(text: str, path: Path) -> tuple[dict, str]:
    """The `key: value` / `key: [a, b]` block between two --- lines, and the body after it."""
    if not text.startswith("---\n"):
        raise SystemExit(f"{path}: no front matter")
    head, _, body = text[4:].partition("\n---\n")
    meta: dict = {}
    for line in head.splitlines():
        if not line.strip():
            continue
        key, sep, value = line.partition(":")
        if not sep:
            raise SystemExit(f"{path}: front matter line {line!r}")
        value = value.strip()
        if value.startswith("[") and value.endswith("]"):
            meta[key.strip()] = [v.strip() for v in value[1:-1].split(",") if v.strip()]
        else:
            meta[key.strip()] = value
    return meta, body


def topic_id(path: Path) -> str:
    return path.relative_to(ROOT / "topics").with_suffix("").as_posix()


def target(source: Path, href: str) -> Path:
    return (source.parent / href).resolve()


def slug(title: str) -> str:
    """The anchor docstream and GitHub give a heading: lower case, spaces to hyphens, punctuation dropped."""
    return re.sub(r"[^\w一-鿿-]", "", title.strip().lower().replace(" ", "-"))


def main() -> None:
    topics, courses, materials = {}, [], []
    for path in sorted((ROOT / "topics").rglob("*.md")):
        meta, body = front(path.read_text(encoding="utf-8"), path)
        tid = topic_id(path)
        topics[tid] = {"id": tid, "title": meta["title"], "requires": meta.get("requires", []), "path": path,
                       "taught_by": [], "tested_by": [], "leads_to": []}
    for tid, t in topics.items():
        for need in t["requires"]:
            if need not in topics:
                raise SystemExit(f"topics/{tid}.md requires {need}, which is no topic")
            topics[need]["leads_to"].append(tid)

    def linked_topics(path: Path, text: str) -> list[str]:
        found = []
        for _, href, _ in LINK.findall(text):
            dest = target(path, href)
            if ROOT / "topics" in dest.parents:
                tid = dest.relative_to(ROOT / "topics").with_suffix("").as_posix()
                if tid not in topics:
                    raise SystemExit(f"{path.relative_to(ROOT)} links {href}, which is no topic")
                found.append(tid)
            elif not dest.exists():
                raise SystemExit(f"{path.relative_to(ROOT)} links {href}, which does not exist")
        return found

    for path in sorted((ROOT / "courses").glob("*.md")):
        meta, body = front(path.read_text(encoding="utf-8"), path)
        if meta["code"] != path.stem:
            raise SystemExit(f"{path.name}: code {meta['code']} is not its file name")
        chapters = []
        for block in re.split(r"^## ", body, flags=re.M)[1:]:
            title, _, rest = block.partition("\n")
            ids = linked_topics(path, rest)
            chapters.append({"title": title.strip(), "topics": ids})
            for tid in ids:
                topics[tid]["taught_by"].append(meta["code"])
        courses.append({"code": meta["code"], "name": meta["name"], "former": meta.get("former", []),
                        "subject": meta["subject"], "chapters": chapters, "path": path.relative_to(ROOT).as_posix()})

    for path in sorted((ROOT / "materials").rglob("*.md")):
        meta, body = front(path.read_text(encoding="utf-8"), path)
        rel = path.relative_to(ROOT).as_posix()
        questions, heading = [], None
        for line in body.splitlines():
            m = HEADING.match(line)
            if m:
                heading = m.group(2)
            elif line.startswith("知识点："):
                if heading is None:
                    raise SystemExit(f"{rel}: a 知识点 line before any heading")
                ids = linked_topics(path, line)
                if not ids:
                    raise SystemExit(f"{rel}: 知识点 under {heading} links no topic")
                questions.append({"heading": heading, "anchor": slug(heading), "topics": ids})
                for tid in ids:
                    topics[tid]["tested_by"].append({"material": rel, "heading": heading, "anchor": slug(heading)})
        linked_topics(path, body)
        materials.append({"path": rel, "title": meta["title"], "kind": meta["kind"], "course": meta["course"],
                          "term": meta.get("term"), "source": meta["source"], "questions": len(questions)})

    if OUT.exists():
        shutil.rmtree(OUT)
    for folder in ("courses", "topics", "materials"):
        shutil.copytree(ROOT / folder, OUT / folder)
    index = {
        "courses": courses,
        "topics": [{k: (v.relative_to(ROOT).as_posix() if k == "path" else v) for k, v in t.items()}
                   for t in topics.values()],
        "materials": materials,
    }
    (OUT / "knowledge.json").write_text(json.dumps(index, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    cited = sum(len(t["tested_by"]) for t in topics.values())
    print(f"{len(courses)} courses, {len(topics)} topics, {len(materials)} materials, {cited} question links")


if __name__ == "__main__":
    sys.exit(main())
