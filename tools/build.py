"""Check every link in the knowledge and write what readers need: build/knowledge.json and the documents beside it.

    courses/<subject>.md     a subject's outline: chapters in teaching order, each a list of topic links; the course
                             codes taught now (codes) and before (former) that teach it
    topics/<subject>/<t>.md  one topic; `requires:` names the topics it builds on
    materials/<src>/<code>/  one source document made into Markdown, each question under its own heading
                             with a 知识点 line linking the topics it tests

A topic's backlinks (the courses that teach it, the questions that test it, the topics built on it) are computed here,
never written by hand. Any link to something that does not exist stops the build.

Pictures are not in build/: each goes to build-media/k<n>/ by a hash of its path, one folder per EdgeOne Makers
project (a project holds at most 20,000 files), and the documents name them by their full address there. Readers fetch
pictures straight from those static hosts, close to them and free of any function; build/ stays text.
"""
from __future__ import annotations

import json
import re
import shutil
import sys
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "build"
MEDIA_OUT = ROOT / "build-media"
# One host per Makers project; add one when a shard nears 20,000 files (every picture then moves once).
MEDIA = ["https://k1.hicancan.top", "https://k2.hicancan.top", "https://k3.hicancan.top"]
MEDIA_HEADERS = {"headers": [{"source": "/*", "headers": [
    {"key": "Cache-Control", "value": "public, max-age=86400, stale-while-revalidate=604800"},
    {"key": "Access-Control-Allow-Origin", "value": "*"},
    {"key": "X-Content-Type-Options", "value": "nosniff"}]}]}


def shard(rel: str) -> int:
    """Which media host keeps a picture: FNV-1a of its path, so the choice never depends on what else exists."""
    value = 0x811C9DC5
    for byte in rel.encode("utf-8"):
        value = ((value ^ byte) * 0x01000193) & 0xFFFFFFFF
    return value % len(MEDIA)


def media_url(rel: str) -> str:
    return f"{MEDIA[shard(rel)]}/{urllib.parse.quote(rel)}"
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
    """A question's anchor: its heading with spaces as hyphens, which every reader computes the same way."""
    return re.sub(r"\s+", "-", title.strip())


IMAGE = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)\)")


def published(path: Path, body: str) -> str:
    """A document as readers get it: no front matter, every link and image as a path from the knowledge's root."""
    def rooted(href: str) -> str:
        return target(path, href).relative_to(ROOT).as_posix()
    body = IMAGE.sub(lambda m: f"![{m.group(1)}]({media_url(rooted(m.group(2)))})", body)
    return LINK.sub(lambda m: f"[{m.group(1)}]({rooted(m.group(2))}{m.group(3) or ''})", body)


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
        if not meta.get("codes"):
            raise SystemExit(f"{path.name}: names no course code taught now")
        chapters = []
        for block in re.split(r"^## ", body, flags=re.M)[1:]:
            title, _, rest = block.partition("\n")
            ids = linked_topics(path, rest)
            chapters.append({"title": title.strip(), "topics": ids})
            for tid in ids:
                topics[tid]["taught_by"].append(path.stem)
        courses.append({"id": path.stem, "name": meta["name"], "codes": meta["codes"], "former": meta.get("former", []),
                        "chapters": chapters, "path": path.relative_to(ROOT).as_posix()})

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
        if not (ROOT / "courses" / f"{meta['course']}.md").exists():
            raise SystemExit(f"{rel}: course {meta['course']} has no courses/{meta['course']}.md")
        materials.append({"path": rel, "title": meta["title"], "kind": meta["kind"], "course": meta["course"],
                          "term": meta.get("term"), "source": meta["source"], "questions": len(questions)})

    for out in (OUT, MEDIA_OUT):
        if out.exists():
            shutil.rmtree(out)
    pictures = [0] * len(MEDIA)
    for folder in ("courses", "topics", "materials"):
        for source in (ROOT / folder).rglob("*"):
            if source.is_dir():
                continue
            rel = source.relative_to(ROOT).as_posix()
            if source.suffix == ".md":
                dest = OUT / rel
                dest.parent.mkdir(parents=True, exist_ok=True)
                _, body = front(source.read_text(encoding="utf-8"), source)
                dest.write_text(published(source, body).lstrip("\n"), encoding="utf-8")
            else:
                n = shard(rel)
                pictures[n] += 1
                dest = MEDIA_OUT / f"k{n + 1}" / rel
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(source, dest)
    for n, count in enumerate(pictures):
        if count > 19000:
            raise SystemExit(f"media host k{n + 1} would hold {count} files; add a host to MEDIA")
        folder = MEDIA_OUT / f"k{n + 1}"
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "edgeone.json").write_text(json.dumps(MEDIA_HEADERS, indent=1) + "\n", encoding="utf-8")
        (folder / "index.html").write_text("<!doctype html><title>njupt-knowledge</title>Pictures of njupt-knowledge.\n", encoding="utf-8")
    index = {
        "courses": courses,
        "topics": [{k: (v.relative_to(ROOT).as_posix() if k == "path" else v) for k, v in t.items()}
                   for t in topics.values()],
        "materials": materials,
        "media": MEDIA,
    }
    (OUT / "knowledge.json").write_text(json.dumps(index, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    cited = sum(len(t["tested_by"]) for t in topics.values())
    print(f"{len(courses)} courses, {len(topics)} topics, {len(materials)} materials, {cited} question links; pictures {pictures}")


if __name__ == "__main__":
    sys.exit(main())
