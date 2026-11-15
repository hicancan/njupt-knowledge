"""Compile one subject: every source file of it in, courses/ topics/ materials/ out.

    python -m tools.compile.run --subject 计算机通信与网络 --domain 计算机网络 --codes JS160201S \\
        --former B0301152S --select cs-free:【B0301152S】计算机通信与网络/

0 pages     each file becomes pages: Office exports to PDF, MinerU reads every page, figures cut out
1 classify  what each document is; whole published books only inform the outline
2 slides    a slide deck is shown as its slides, each picture with the text read from it; no model rewrites it
  questions a paper, exercise or answer sheet is rewritten into question cards by fast models, in parallel
3 outline   the subject's chapters and topics, from the decks' slide titles and the review outlines
4 link      every question to the topics it tests; a question the source left unanswered is solved
5 explain   every topic written from its slides and questions
6 emit      the files; decoration figures dropped; what failed listed in review/<subject>.md
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import threading
import urllib.parse
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import pymupdf
from PIL import Image

from . import agents
from .pages import FIGURES, OFFICE, pages_of
from .pool import Pool
from .store import WORK

ROOT = Path(__file__).resolve().parents[2]
SOURCES = {"cs-free": (WORK / "cs-free", "https://github.com/NJUPTFreeExams/NJUPT-CS-FREE/blob/main/"),
           "batch-2": (Path(r"D:\Data\另一批资料"), None)}
UNPACKED = WORK / "unpacked"
READABLE = {".pdf", ".doc", ".docx", ".ppt", ".pptx", ".jpg", ".jpeg", ".png", ".txt", ".md"}
QUESTION_KINDS = {"期末试卷", "答案", "习题"}
SLIDE_KINDS = {"课件"}
CHUNK = 7000            # characters of source a fast model rewrites at once
SLIDE_WIDTH = 1100
office = threading.Lock()
FAILED: list[str] = []


def log(*parts: object) -> None:
    print(*parts, flush=True)


PROGRESS: dict[str, int] = {}
PROGRESS_LOCK = threading.Lock()


def safe(what, task, fallback=None, stage: str = "", total: int = 0):
    """task's result; a task no model could do is listed for review instead of stopping the run. With a stage name,
    every finished item is counted and the count logged now and then, so a run that stops moving is seen at once."""
    def run(item):
        try:
            return task(item)
        except Exception as error:  # noqa: BLE001 - one failed item must not stop a subject
            FAILED.append(f"- {what(item)}：{str(error)[:200]}")
            return fallback
        finally:
            if stage:
                with PROGRESS_LOCK:
                    done = PROGRESS[stage] = PROGRESS.get(stage, 0) + 1
                if done == total or done % max(1, total // 20) == 0:
                    log(f"  {stage} {done}/{total} {time.strftime('%H:%M:%S')}")
    return run


def selected(selectors: list[str]) -> list[dict]:
    """Inventory rows under each source:prefix, without duplicates and without what cannot be read."""
    rows = []
    for selector in selectors:
        source, prefix = selector.split(":", 1)
        for line in (ROOT / "sources" / f"{source}.jsonl").read_text(encoding="utf-8").splitlines():
            row = json.loads(line)
            if "sha256" not in row or row["duplicates"] or not row["path"].startswith(prefix):
                continue
            if Path(row["path"]).suffix.lower() not in READABLE or row["kind"] == "软件":
                continue
            if "/__MACOSX/" in f"/{row['path']}" or Path(row["path"]).name.startswith("._"):
                continue
            root, url = SOURCES[source]
            parts = row["path"].split("/")
            archive = next((i for i, part in enumerate(parts) if Path(part).suffix.lower() in (".zip", ".rar", ".7z")), None)
            local = (UNPACKED / source / "/".join(parts[:archive + 1]) / "/".join(parts[archive + 1:])) if archive is not None else root / row["path"]
            rows.append({**row, "source": source, "local": local,
                         "url": url + urllib.parse.quote(row["path"]) if url and archive is None else f"{source}:{row['path']}"})
    return rows


def formulas(text: str) -> str:
    """Formulas in the delimiters docstream reads: \\( \\) becomes $ $, \\[ \\] becomes $$ $$ on lines of their own;
    also puts GitHub Alert tags (> [!IMPORTANT] ...) on their own first blockquote line so docstream parses them."""
    text = re.sub(r"(?m)^>\s*(\[\!(?:NOTE|TIP|IMPORTANT|WARNING|CAUTION)\])[ \t]+(\S[^\n]*)", r"> \1\n> \2", text)
    text = re.sub(r"\\\[\s*(.+?)\s*\\\]", lambda m: f"\n$$\n{m.group(1)}\n$$\n", text, flags=re.S)
    return re.sub(r"\\\(\s*(.+?)\s*\\\)", lambda m: f"${m.group(1)}$", text, flags=re.S)


def slug(title: str) -> str:
    return re.sub(r"[\\/:*?\"<>|\s]+", "-", re.sub(r"[《》（）()]", "", title)).strip("-")[:60]


def questions_of(body: str) -> list[tuple[str, str]]:
    parts = re.split(r"^### ", body, flags=re.M)
    return [(part.split("\n", 1)[0].strip(), part) for part in parts[1:]]


def chunks(pages: list[dict]) -> list[list[dict]]:
    """Pages grouped to about CHUNK characters each: a dense scanned page stands alone, light pages go many at once."""
    groups, size = [[]], 0
    for page in pages:
        length = len(page["markdown"])
        if groups[-1] and size + length > CHUNK:
            groups.append([])
            size = 0
        groups[-1].append(page)
        size += length
    return [group for group in groups if group]


def slide_title(markdown: str, number: int) -> str:
    for line in markdown.splitlines():
        text = re.sub(r"^#+\s*|!\[[^\]]*\]\([^)]*\)|<[^>]+>", "", line).strip(" *_")
        if 2 <= len(text) <= 40:
            return text
    return f"第 {number} 页"


def slide_text(markdown: str) -> str:
    """A slide's text as plain lines beneath its picture: no figures, no headings."""
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", markdown)
    text = re.sub(r"^#+\s*", "", text, flags=re.M)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def decorative(body: str) -> set[str]:
    """Figures that are template decoration: the same picture on three or more pages, or too small to be a figure."""
    seen: dict[str, set[str]] = {}
    small = set()
    for ref in set(re.findall(r"\(figure:([^)\s]+)\)", body)):
        if not ref or ref in (".", "..") or "/" in ref or "\\" in ref:
            continue
        path = FIGURES / ref
        try:
            if not path.is_file():
                continue
            seen.setdefault(hashlib.sha256(path.read_bytes()).hexdigest(), set()).add(ref)
            with pymupdf.open(path) as image:
                rect = image[0].rect
                if rect.width < 60 or rect.height < 60:
                    small.add(ref)
        except OSError:
            continue
    return {ref for refs in seen.values() if len(refs) >= 3 for ref in refs} | small


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--subject", required=True)
    parser.add_argument("--domain", required=True)
    parser.add_argument("--codes", required=True)
    parser.add_argument("--former", default="")
    parser.add_argument("--select", action="append", required=True)
    parser.add_argument("--workers", type=int, default=24)
    args = parser.parse_args()
    pool = Pool()
    run = ThreadPoolExecutor(max_workers=args.workers)
    files = selected(args.select)
    log(f"{args.subject}: {len(files)} files")

    # 0 pages
    def paged(row):
        return pages_of(row["local"], row["sha256"])
    for row, pages in zip(files, run.map(safe(lambda r: f"{r['path']} 的解析", paged, []), files)):
        row["pages"] = pages
    files = [row for row in files if row["pages"]]
    log("pages:", sum(len(row["pages"]) for row in files))

    # 1 classify
    for row, meta in zip(files, run.map(safe(lambda r: f"{r['path']} 的分类", lambda r: agents.classify(
            pool, r["path"], "\n".join(p["markdown"] for p in r["pages"][:3]), args.subject)), files)):
        row["meta"] = meta
    books = [row for row in files if row["meta"] and row["meta"]["book"]]
    documents = [row for row in files if row["meta"] and not row["meta"]["book"] and row["meta"]["subject_matches"]]
    log(f"classified: {len(documents)} to compile, {len(books)} books for the outline only")

    # 2 slides stay slides; everything else is rewritten into the format by fast models
    stretches = []
    for row in documents:
        if row["meta"]["kind"] in SLIDE_KINDS:
            row["body"] = None
            continue
        groups = chunks(row["pages"])
        for n, group in enumerate(groups):
            part = f"第 {n + 1} 部分（共 {len(groups)} 部分）" if len(groups) > 1 else ""
            stretches.append((row, part, f"第 {group[0]['number']}–{group[-1]['number']} 页", "\n\n".join(p["markdown"] for p in group)))
    texts = list(run.map(safe(lambda job: f"{job[0]['meta']['title']} {job[2]} 的整理（已用识别原文代替）",
                              lambda job: agents.normalize(pool, job[0]["meta"]["title"], job[0]["meta"]["kind"], job[1], job[2], job[3])), stretches))
    for row in documents:
        if row["meta"]["kind"] in SLIDE_KINDS:
            continue
        row["body"] = "\n\n".join(text if text is not None else job[3] for job, text in zip(stretches, texts) if job[0] is row)
    log(f"rewrote {len(stretches)} stretches; {sum(1 for r in documents if r['meta']['kind'] in SLIDE_KINDS)} decks kept as slides")

    # 3 outline, from slide titles and the headings of everything else
    evidence = []
    for row in documents + books:
        if row in documents and row["meta"]["kind"] in SLIDE_KINDS:
            heads = [slide_title(p["markdown"], p["number"]) for p in row["pages"]]
        else:
            heads = re.findall(r"^#{2,3} .+$", row.get("body") or "", re.M) or [p["markdown"][:200] for p in row["pages"][:8]]
        evidence.append(f"## {row['meta']['title']}（{row['meta']['kind']}）\n" + "\n".join(dict.fromkeys(heads))[:3000])
    # The frame is made once and kept in the repository: topic ids are what links, notes and readers point at, so a
    # later run (with more material) grows the published frame by hand or on purpose, never by drifting.
    subject_slug = slug(args.subject)
    kept = ROOT / "outlines" / f"{subject_slug}.json"
    if kept.exists():
        frame = json.loads(kept.read_text(encoding="utf-8"))
    else:
        frame = agents.outline(pool, args.subject, args.domain, "\n\n".join(evidence))
        frame.pop("model", None)
        kept.parent.mkdir(parents=True, exist_ok=True)
        kept.write_text(json.dumps(frame, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    topics = [{**topic, "chapter": chapter["title"]} for chapter in frame["chapters"] for topic in chapter["topics"]]
    titles = {t["id"]: t["title"] for t in topics}
    log("outline:", len(frame["chapters"]), "chapters,", len(topics), "topics")

    # 4 link, and solve what the source left unanswered
    asked = [(row, heading, block) for row in documents if row["meta"]["kind"] in QUESTION_KINDS | {"复习要点"} and row.get("body")
             for heading, block in questions_of(row["body"])]
    links = list(run.map(safe(lambda q: f"{q[0]['meta']['title']} · {q[1]} 的知识点", lambda q: agents.link(pool, args.subject, topics, q[2]), [], "link", len(asked)), asked))
    unanswered = [i for i, (row, _, block) in enumerate(asked) if row["meta"]["kind"] in QUESTION_KINDS and not re.search(r"^(答案|参考解答)：", block, re.M)]
    solved = dict(zip(unanswered, run.map(safe(lambda i: f"{asked[i][0]['meta']['title']} · {asked[i][1]} 的解答", lambda i: agents.solve(pool, args.subject, asked[i][2]), None, "solve", len(unanswered)), unanswered)))
    log(f"linked {len(asked)} questions, solved {len(unanswered)}")

    # 5 explain, from the slides of the topic's chapter and the questions that test it
    by_topic: dict[str, list[str]] = {}
    for (row, heading, block), ids in zip(asked, links):
        for tid in ids or []:
            by_topic.setdefault(tid, []).append(block)
    deck_text = {row["meta"]["title"]: "\n".join(slide_text(p["markdown"]) for p in row["pages"]) for row in documents if row["meta"]["kind"] in SLIDE_KINDS}
    outlines = "\n".join(row.get("body") or "" for row in documents if row["meta"]["kind"] == "复习要点")

    def note(topic):
        words = [w for w in re.split(r"[（）()、，,\s/与和]+", topic["title"]) if len(w) >= 2]
        number = re.search(r"第\s*(\d+)\s*章", topic["chapter"])
        decks = [text for title, text in deck_text.items() if number and re.search(rf"第\s*{number.group(1)}\s*章", title)] or list(deck_text.values())
        lines = [line for text in decks + [outlines] for line in text.split("\n") if any(w in line for w in words)]
        return agents.explain(pool, args.subject, topic, topic["chapter"], "\n".join(lines[:240]), "\n\n".join(by_topic.get(topic["id"], [])[:6]))
    notes = dict(zip([t["id"] for t in topics], run.map(safe(lambda t: f"知识点 {t['title']} 的讲解", note, None, "explain", len(topics)), topics)))
    log("explained", len(notes), "topics")

    # 6 emit
    domain = ROOT / "topics" / args.domain
    domain.mkdir(parents=True, exist_ok=True)
    for topic in topics:
        body = (notes[topic["id"]] or {}).get("body") or "（讲解还没写好。）"
        requires = ", ".join(f"{args.domain}/{r}" for r in topic["requires"] if r in titles)
        (domain / f"{topic['id']}.md").write_text(f"---\ntitle: {topic['title']}\nrequires: [{requires}]\n---\n\n# {topic['title']}\n\n{formulas(body)}\n", encoding="utf-8")
    course = [f"---\nname: {args.subject}\ncodes: [{args.codes}]\nformer: [{args.former}]\n---\n\n# {args.subject}\n",
              f"南京邮电大学《{args.subject}》。章节和知识点由课件、历年复习提纲整理。\n"]
    for chapter in frame["chapters"]:
        course += [f"## {chapter['title']}\n", *[f"- [{t['title']}](../topics/{args.domain}/{t['id']}.md)" for t in chapter["topics"]], ""]
    (ROOT / "courses" / f"{subject_slug}.md").write_text("\n".join(course) + "\n", encoding="utf-8")

    link_of = {(id(row), heading): ids for (row, heading, _), ids in zip(asked, links)}
    solution_of = {(id(asked[i][0]), asked[i][1]): s for i, s in solved.items() if s}
    # 6 emit slides in parallel (reusing up-to-date WebP images) & write materials
    def _write_slide(job):
        src, dst = job
        with Image.open(src) as image:
            image.thumbnail((SLIDE_WIDTH, SLIDE_WIDTH))
            image.save(dst, "WEBP", quality=62)

    slide_jobs, expected_assets = [], {}
    for row in documents:
        meta = row["meta"]
        name = slug(meta["title"])
        folder = ROOT / "materials" / row["source"] / (args.former.split(",")[0].strip() if args.former else args.subject)
        assets = folder / f"{name}.assets"
        assets.mkdir(parents=True, exist_ok=True)
        keep: set[str] = set()
        if meta["kind"] in SLIDE_KINDS:
            for page in row["pages"]:
                fname = f"第{page['number']}页.webp"
                keep.add(fname)
                picture = assets / fname
                if not picture.exists() or picture.stat().st_mtime < Path(page["image"]).stat().st_mtime:
                    slide_jobs.append((page["image"], picture))
        expected_assets[id(row)] = (folder, assets, keep)
    if slide_jobs:
        list(run.map(safe(lambda j: f"幻灯片转码 {j[1].name}", _write_slide), slide_jobs))

    for row in documents:
        meta = row["meta"]
        name = slug(meta["title"])
        folder, assets, keep = expected_assets[id(row)]
        if meta["kind"] in SLIDE_KINDS:
            if assets.exists():
                for stale in list(assets.iterdir()):
                    if stale.name not in keep:
                        stale.unlink()
            parts = []
            for page in row["pages"]:
                text = slide_text(page["markdown"])
                parts.append(f"### {slide_title(page['markdown'], page['number'])}\n\n![第 {page['number']} 页]({name}.assets/第{page['number']}页.webp)\n"
                             + (f"\n原文：\n\n{text}\n" if text else ""))
            body = "\n".join(parts)
        else:
            if assets.exists():
                for stale in list(assets.iterdir()):
                    stale.unlink()
            count = 0
            refs = sorted(set(re.findall(r"!\[([^\]]*)\]\(figure:([^)\s]+)\)", row["body"])), key=lambda pair: pair[1])
            refs = [pair for pair in refs if pair[1] not in (".", "..") and (FIGURES / pair[1]).is_file()]
            verdicts = run.map(safe(lambda pair: f"图 {pair[1]} 的判断", lambda pair: agents.figure_matters(pool, FIGURES / pair[1], pair[0]), True), refs)
            decorations = decorative(row["body"]) | {ref for (_, ref), keep in zip(refs, verdicts) if not keep}

            def figure(match):
                nonlocal count
                if match.group(2) in (".", ".."):
                    return ""
                source = FIGURES / match.group(2)
                if not source.is_file() or match.group(2) in decorations:
                    return ""
                count += 1
                assets.mkdir(parents=True, exist_ok=True)
                target = assets / f"图{count}{source.suffix}"
                shutil.copyfile(source, target)
                return f"![{match.group(1) or f'图 {count}'}]({name}.assets/{target.name})"
            body = re.sub(r"!\[([^\]]*)\]\(figure:([^)\s]+)\)", figure, row["body"])
            body = re.sub(r"(?m)^知识点：[^\n]*\n?", "", body)
            body = re.sub(r"\[([^\]]+)\]\(([^)\s]+\.md)(#[^)]*)?\)", lambda m: m.group(1), body)
            out = []
            for part in re.split(r"(?=^### )", body, flags=re.M):
                heading = part[4:].split("\n", 1)[0].strip() if part.startswith("### ") else None
                ids = link_of.get((id(row), heading)) if heading else None
                if ids:
                    part = part.rstrip()
                    solution = solution_of.get((id(row), heading))
                    if solution:
                        part += f"\n\n参考解答：{solution['answer']}"
                    part += "\n\n知识点：" + "、".join(f"[{titles[t]}](../../../topics/{args.domain}/{t}.md)" for t in ids if t in titles) + "\n\n"
                out.append(part)
            body = "".join(out)
        if assets.exists() and not any(assets.iterdir()):
            assets.rmdir()
        front = f"---\ntitle: {meta['title']}\nkind: {meta['kind']}\ncourse: {subject_slug}\n" + (f"term: {meta['term']}\n" if meta.get("term") else "") + f"source: {row['url']}\n---\n\n"
        intro = f"# {meta['title']}\n\n" + ("原件的每一页，下面附识别出的文字。\n\n" if meta["kind"] in SLIDE_KINDS else "原件经识别和整理；“参考解答”是我们补的。\n\n")
        (folder / f"{name}.md").write_text(front + intro + formulas(body).strip() + "\n", encoding="utf-8")

    review = ROOT / "review" / f"{subject_slug}.md"
    review.parent.mkdir(exist_ok=True)
    review.write_text(f"# 《{args.subject}》待核对\n\n" + ("\n".join(FAILED) if FAILED else "没有。") + "\n", encoding="utf-8")
    log(f"emitted {len(documents)} materials, {len(topics)} topics; {len(FAILED)} to review")


if __name__ == "__main__":
    main()
