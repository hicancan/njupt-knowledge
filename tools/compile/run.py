"""Compile one subject: every source file of it in, courses/ topics/ materials/ out.

    python -m tools.compile.run --subject 计算机通信与网络 --domain 计算机网络 --codes JS160201S \\
        --former B0301152S --select cs-free:【B0301152S】计算机通信与网络/

0 pages     each file becomes pages: Office exports to PDF, MinerU reads every page (4 accounts), figures cut out
1 classify  what each document is; whole published books only inform the outline
2 normalize every stretch of eight pages rewritten in the format by a text model, in parallel
4 outline   the subject's chapters and topics, from slides, review outlines and book contents
5 link      every question to the topics it tests; unanswered questions solved and checked by another model
6 explain   every topic written from the course's slides and questions, reviewed by another model
7 emit      the files, figures cut from the pages; disagreements listed in review/<subject>.md
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import threading
import urllib.parse
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from . import agents
from .pages import FIGURES, OFFICE, pages_of
from .pool import Pool
from .store import WORK

ROOT = Path(__file__).resolve().parents[2]
SOURCES = {"cs-free": (WORK / "cs-free", "https://github.com/NJUPTFreeExams/NJUPT-CS-FREE/blob/main/"),
           "batch-2": (Path(r"D:\Data\另一批资料"), None)}
UNPACKED = WORK / "unpacked"
READABLE = {".pdf", ".doc", ".docx", ".ppt", ".pptx", ".jpg", ".jpeg", ".png", ".txt", ".md"}
QUESTION_KINDS = {"期末试卷", "答案", "习题", "复习要点"}
office = threading.Lock()


def log(*parts: object) -> None:
    print(*parts, flush=True)


FAILED: list[str] = []


def safe(what: str, task, fallback=None):
    """task's result; a task no model could do is listed for review instead of stopping the run."""
    def run(item):
        try:
            return task(item)
        except Exception as error:  # noqa: BLE001 - one failed item must not stop a subject
            FAILED.append(f"- {what(item)}：{str(error)[:200]}")
            return fallback
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
            root, url = SOURCES[source]
            parts = row["path"].split("/")
            archive = next((i for i, part in enumerate(parts) if Path(part).suffix.lower() in (".zip", ".rar", ".7z")), None)
            local = (UNPACKED / source / "/".join(parts[:archive + 1]) / "/".join(parts[archive + 1:])) if archive is not None else root / row["path"]
            rows.append({**row, "source": source, "local": local,
                         "url": url + urllib.parse.quote(row["path"]) if url and archive is None else f"{source}:{row['path']}"})
    return rows


def slug(title: str) -> str:
    return re.sub(r"[\\/:*?\"<>|\s]+", "-", re.sub(r"[《》（）()]", "", title)).strip("-")[:60]


def questions_of(body: str) -> list[tuple[str, str]]:
    """(heading, block) for every ### section."""
    parts = re.split(r"^### ", body, flags=re.M)
    return [(part.split("\n", 1)[0].strip(), part) for part in parts[1:]]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--subject", required=True)
    parser.add_argument("--domain", required=True)
    parser.add_argument("--codes", required=True)
    parser.add_argument("--former", default="")
    parser.add_argument("--select", action="append", required=True)
    parser.add_argument("--workers", type=int, default=12)
    args = parser.parse_args()
    pool = Pool()
    files = selected(args.select)
    log(f"{len(files)} files")
    run = ThreadPoolExecutor(max_workers=args.workers)

    # 0 pages
    def paged(row):
        if Path(row["path"]).suffix.lower() in OFFICE:
            with office:
                return pages_of(row["local"], row["sha256"])
        return pages_of(row["local"], row["sha256"])
    for row, pages in zip(files, run.map(paged, files)):
        row["pages"] = pages
    log("pages:", sum(len(row["pages"]) for row in files))

    # 1 classify
    for row, kind in zip(files, run.map(lambda r: agents.classify(pool, r["path"], "\n".join(p["markdown"] for p in r["pages"][:3]), args.subject), files)):
        row["meta"] = kind
    books = [row for row in files if row["meta"]["book"]]
    documents = [row for row in files if not row["meta"]["book"] and row["meta"]["subject_matches"]]
    log(f"classified: {len(documents)} to compile, {len(books)} books for the outline only")

    # 2 normalize, eight pages at a time, every stretch in parallel
    stretches = []
    for row in documents:
        groups = [row["pages"][i:i + 8] for i in range(0, len(row["pages"]), 8)]
        for n, group in enumerate(groups):
            part = f"第 {n + 1} 部分（共 {len(groups)} 部分）" if len(groups) > 1 else ""
            pages = f"第 {group[0]['number']}–{group[-1]['number']} 页"
            stretches.append((row, n, part, pages, "\n\n".join(p["markdown"] for p in group)))
    normalized = list(run.map(lambda job: agents.normalize(pool, job[0]["meta"]["title"], job[0]["meta"]["kind"], job[2], job[3], job[4]), stretches))
    for row in documents:
        row["body"] = "\n\n".join(text for (owner, *_), text in zip(stretches, normalized) if owner is row)
    log("normalized", len(stretches), "stretches of", len(documents), "documents")

    # 4 outline
    evidence = []
    for row in documents + books:
        heads = re.findall(r"^#{2,3} .+$", row.get("body", ""), re.M) or [p["markdown"][:200] for p in row["pages"][:8]]
        evidence.append(f"## {row['meta']['title']}（{row['meta']['kind']}）\n" + "\n".join(heads[:80]))
    frame = agents.outline(pool, args.subject, args.domain, "\n\n".join(evidence))
    topics = [{**topic, "chapter": chapter["title"]} for chapter in frame["chapters"] for topic in chapter["topics"]]
    log("outline:", len(frame["chapters"]), "chapters,", len(topics), "topics")

    # 5 link and solve
    review: list[str] = []
    asked = [(row, heading, block) for row in documents if row["meta"]["kind"] in QUESTION_KINDS for heading, block in questions_of(row["body"])]
    links = list(run.map(safe(lambda q: f"{q[0]['meta']['title']} · {q[1]} 的知识点", lambda q: agents.link(pool, args.subject, topics, q[2]), []), asked))
    unanswered = [i for i, (_, _, block) in enumerate(asked) if not re.search(r"^(答案|参考解答)：", block, re.M)]
    solutions = dict(zip(unanswered, run.map(safe(lambda i: f"{asked[i][0]['meta']['title']} · {asked[i][1]} 的解答", lambda i: agents.solve(pool, args.subject, asked[i][2])), unanswered)))
    log(f"linked {len(asked)} questions, solved {len(unanswered)}")

    # 6 explain
    by_topic: dict[str, list[str]] = {}
    for (row, heading, block), ids in zip(asked, links):
        for tid in ids:
            by_topic.setdefault(tid, []).append(block)
    slides = {row["meta"]["title"]: row["body"] for row in documents if row["meta"]["kind"] in ("课件", "复习要点")}

    def note(topic):
        words = [w for w in re.split(r"[（）()、，,\s/与和]+", topic["title"]) if len(w) >= 2]
        lines = [line for text in slides.values() for line in text.split("\n") if any(w in line for w in words)]
        return agents.explain(pool, args.subject, topic, topic["chapter"], "\n".join(lines[:200]), "\n\n".join(by_topic.get(topic["id"], [])[:6]))
    notes = dict(zip([t["id"] for t in topics], run.map(safe(lambda t: f"知识点 {t['title']} 的讲解", note), topics)))
    log("explained", len(notes), "topics")

    # 7 emit
    domain = ROOT / "topics" / args.domain
    domain.mkdir(parents=True, exist_ok=True)
    titles = {t["id"]: t["title"] for t in topics}
    for topic in topics:
        result = notes[topic["id"]] or {"body": "（讲解还没写好。）", "reviewed": {"ok": True}}
        if not result["reviewed"].get("ok"):
            review.append(f"- 知识点 {topic['title']}：审读意见已改入，原意见：{result['reviewed'].get('fixes', '')[:300]}")
        requires = ", ".join(f"{args.domain}/{r}" for r in topic["requires"] if r in titles)
        (domain / f"{topic['id']}.md").write_text(f"---\ntitle: {topic['title']}\nrequires: [{requires}]\n---\n\n# {topic['title']}\n\n{result['body']}\n", encoding="utf-8")

    course = [f"---\nname: {args.subject}\ncodes: [{args.codes}]\nformer: [{args.former}]\n---\n\n# {args.subject}\n",
              f"南京邮电大学《{args.subject}》。章节和知识点由课件、历年复习提纲和教材目录整理。\n"]
    for chapter in frame["chapters"]:
        course.append(f"## {chapter['title']}\n")
        course += [f"- [{t['title']}](../topics/{args.domain}/{t['id']}.md)" for t in chapter["topics"]]
        course.append("")
    (ROOT / "courses" / f"{args.subject}.md").write_text("\n".join(course) + "\n", encoding="utf-8")

    links_of = {(id(row), heading): ids for (row, heading, _), ids in zip(asked, links)}
    for index, (row, heading, block) in enumerate(asked):
        if index in solutions and solutions[index] and not solutions[index]["correct"]:
            review.append(f"- {row['meta']['title']} · {heading}：两个模型对解答有分歧，{solutions[index]['problem'][:300]}")
    for row in documents:
        name = slug(row["meta"]["title"])
        folder = ROOT / "materials" / row["source"] / (args.former or args.subject)
        assets = folder / f"{name}.assets"
        count = 0

        def figure(match):
            nonlocal count
            source = FIGURES / match.group(2)
            if not source.exists():
                return ""
            count += 1
            target = assets / f"图{count}{source.suffix}"
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
            return f"![{match.group(1) or f'图 {count}'}]({name}.assets/{target.name})"
        body = re.sub(r"!\[([^\]]*)\]\(figure:([^)\s]+)\)", figure, row["body"])
        out = []
        for part in re.split(r"(?=^### )", body, flags=re.M):
            heading = part[4:].split("\n", 1)[0].strip() if part.startswith("### ") else None
            ids = links_of.get((id(row), heading)) if heading else None
            if ids:
                index = next((i for i, q in enumerate(asked) if q[0] is row and q[1] == heading), None)
                solution = solutions.get(index) if index is not None else None
                part = part.rstrip()
                if solution and solution["correct"]:
                    part += f"\n\n参考解答：{solution['answer']}"
                part += "\n\n知识点：" + "、".join(f"[{titles[t]}](../../../topics/{args.domain}/{t}.md)" for t in ids) + "\n\n"
            out.append(part)
        meta = row["meta"]
        front = f"---\ntitle: {meta['title']}\nkind: {meta['kind']}\ncourse: {args.subject}\n" + (f"term: {meta['term']}\n" if meta.get("term") else "") + f"source: {row['url']}\n---\n\n"
        intro = f"# {meta['title']}\n\n原件来自 {row['source']}，经识别和整理；“参考解答”是我们补的。\n\n"
        folder.mkdir(parents=True, exist_ok=True)
        (folder / f"{name}.md").write_text(front + intro + "".join(out).strip() + "\n", encoding="utf-8")

    reviews = ROOT / "review" / f"{args.subject}.md"
    reviews.parent.mkdir(exist_ok=True)
    review += FAILED
    reviews.write_text(f"# 《{args.subject}》待核对\n\n" + ("\n".join(review) if review else "没有。") + "\n", encoding="utf-8")
    log(f"emitted {len(documents)} materials, {len(topics)} topics; {len(review)} items to review")
    log(json.dumps({k: v for k, v in pool.ledger.items()}, ensure_ascii=False))


if __name__ == "__main__":
    main()
