"""Steps 2–6, each one model task with a fixed contract: what goes in, what must come out, and the check it must pass.

The format specification (spec/format.md) is part of every prompt that writes Markdown; a step's VERSION changes when
its prompt does, so the cache redoes exactly that step.
"""
from __future__ import annotations

import re
from pathlib import Path

from .pool import Pool, json_of
from .store import cached


def retried(make, tries: int = 4):
    """make(), again on the next model when its answer fails its check."""
    def run():
        error = None
        for _ in range(tries):
            try:
                return make()
            except (ValueError, KeyError, TypeError) as caught:
                error = caught
        raise RuntimeError(f"no model passed the check: {error}")
    return run

SPEC = (Path(__file__).resolve().parents[2] / "spec" / "format.md").read_text(encoding="utf-8")
KINDS = ["期末试卷", "答案", "复习要点", "习题", "课件", "实验", "教材"]


def classify(pool: Pool, name: str, first_pages: str, subject: str) -> dict:
    """What a document is: kind, a proper title, the term, and whether it is a whole published book."""
    def make():
        prompt = f"""你在整理南京邮电大学《{subject}》的资料。根据文件名和前几页文字判断这份文档：
文件名：{name}
前几页：
{first_pages[:3500]}

只输出 JSON：{{"kind": 从 {KINDS} 中选一个, "title": "规范的中文标题，如“2021—2022 学年第二学期《计算机通信与网络》期末试卷（A卷）”或“《计算机通信与网络》第3章 数据链路层（课件）”", "term": "YYYY-YYYY-N 或 null", "book": 是否为商业出版的整本教材或专著（true/false）, "has_answers": 文档里是否带答案（true/false）, "subject_matches": 内容是否属于《{subject}》（true/false）}}"""
        answer, model = pool.chat("fast", [{"role": "user", "content": prompt}], max_tokens=600)
        value = json_of(answer)
        if value.get("kind") not in KINDS:
            raise ValueError(f"classify gave kind {value.get('kind')}")
        value["model"] = model
        return value
    return cached("classify", 1, (subject, name, first_pages[:3500]), retried(make))


def normalize(pool: Pool, title: str, kind: str, part: str, pages: str, body: str) -> str:
    """A stretch of a document, as MinerU read it, rewritten in the format."""
    def make():
        prompt = f"""你是资料整理员。下面是《{title}》（{kind}）{part}由识别工具读出的内容（{pages}）。把它整理成符合格式规范的 Markdown：

{SPEC}

要求：
- 只整理这里给出的内容，不增删实质内容，不编造；明显的识别错误按上下文改正（错字、断行、乱码、选项挤在一行）。
- 标题层级：## 大题或章，### 题或节；题号写成“题型 序号”，如“### 选择 3”“### 简答 2”；课件按章、节组织。
- 识别工具给出的 HTML 表格改写成 Markdown 表格；公式写成 LaTeX。
- 插图占位 ![…](figure:…) 原样保留在原来的位置，可以补一句替代文字；只是装饰的图标、校徽、页眉横线图可以删掉。
- 原件自带的答案保留，标成“答案：”，放在对应题目下面。
- 页眉页脚、页码、考生须知、装订线、水印都不要。
- 不要 front matter，不要 # 总标题，不要“知识点”行。只输出整理后的 Markdown，不要用代码块包住。

---
{body}"""
        answer, _ = pool.chat("strong", [{"role": "user", "content": prompt}], max_tokens=16000)
        text = re.sub(r"^```(?:markdown)?\s*|\s*```$", "", answer.strip())
        if len(re.sub(r"\s", "", text)) < 0.45 * len(re.sub(r"\s|!\[[^\]]*\]\([^)]*\)", "", body)):
            raise ValueError("normalize dropped too much")
        lost = set(re.findall(r"figure:[^)\s]+", body)) - set(re.findall(r"figure:[^)\s]+", text))
        kept_ratio = 1 - len(lost) / max(1, len(set(re.findall(r"figure:[^)\s]+", body))))
        if kept_ratio < 0.5:
            raise ValueError("normalize dropped most figures")
        return text
    return cached("normalize", 1, (title, kind, part, body), retried(make))


def outline(pool: Pool, subject: str, domain: str, evidence: str) -> dict:
    """The coarse frame: the subject's chapters in teaching order, each with its topics and what they build on."""
    def make():
        prompt = f"""为南京邮电大学《{subject}》搭知识框架。依据是这门课的课件章节、历年复习提纲和教材目录：

{evidence[:24000]}

要求：
- 按讲授顺序列章节；每章列 3～10 个知识点，粒度是“学生复习时会单独掌握的一块”（如“CSMA/CD”“子网划分与 CIDR”“TCP 拥塞控制”），覆盖课件和复习提纲里出现的全部内容。
- 每个知识点给：id（简短中文，可作文件名，不含 / 和空格），title（完整标题，可带括号说明），requires（真正要先懂的其他知识点 id，没有就空）。
- 用这门课自己的术语。

只输出 JSON：{{"chapters": [{{"title": "第1章 概论", "topics": [{{"id": "…", "title": "…", "requires": []}}]}}]}}"""
        answer, model = pool.chat("strong", [{"role": "user", "content": prompt}], think=True, max_tokens=12000)
        value = json_of(answer)
        ids = [topic["id"] for chapter in value["chapters"] for topic in chapter["topics"]]
        if len(ids) != len(set(ids)) or any("/" in i or " " in i for i in ids):
            raise ValueError("outline topic ids are not unique simple names")
        value["model"] = model
        return value
    return cached("outline", 1, (subject, domain, evidence[:24000]), retried(make))


def link(pool: Pool, subject: str, topics: list[dict], question: str) -> list[str]:
    """The topics one question tests, by id."""
    def make():
        listing = "\n".join(f"- {t['id']}：{t['title']}" for t in topics)
        prompt = f"""《{subject}》的一道题，判断它考的是下面哪些知识点（1～3 个，按主次）：

{listing}

题目：
{question[:3000]}

只输出 JSON：{{"topics": ["id", …]}}"""
        answer, _ = pool.chat("fast", [{"role": "user", "content": prompt}], max_tokens=300)
        chosen = [t for t in json_of(answer)["topics"] if t in {x["id"] for x in topics}]
        if not chosen:
            raise ValueError("link chose no known topic")
        return chosen
    return cached("link", 1, (subject, tuple(t["id"] for t in topics), question[:3000]), retried(make))


def solve(pool: Pool, subject: str, question: str) -> dict:
    """A worked answer for a question the source left unanswered, then checked by a model of another family."""
    def make():
        prompt = f"""《{subject}》的一道题。写出参考解答：先给结论，再给简明的推理或计算过程；涉及计算的写出关键步骤；选择题说明为什么选它、其他为什么不对（一句话即可）。用 Markdown，公式用 LaTeX。不要重复题目，不要写“参考解答：”标签。

{question[:4000]}"""
        answer, author = pool.chat("strong", [{"role": "user", "content": prompt}], think=True, max_tokens=4000)
        check = f"""下面是《{subject}》一道题和一份解答。逐步核对解答是否正确。

题目：
{question[:4000]}

解答：
{answer[:5000]}

只输出 JSON：{{"correct": true/false, "problem": "不正确时，具体错在哪里、正确结论是什么；正确时为空"}}"""
        verdict_text, checker = pool.chat("strong", [{"role": "user", "content": check}], think=True, max_tokens=2000,
                                          avoid=author.split(":")[0])
        verdict = json_of(verdict_text)
        return {"answer": answer.strip(), "author": author, "checker": checker,
                "correct": bool(verdict.get("correct")), "problem": verdict.get("problem") or ""}
    return cached("solve", 1, (subject, question[:4000]), retried(make))


def explain(pool: Pool, subject: str, topic: dict, chapter: str, evidence: str, questions: str) -> dict:
    """A topic's note, written from the course's own slides and questions, then reviewed by another family."""
    def make():
        prompt = f"""为南京邮电大学《{subject}》的知识点写讲解正文。

知识点：{topic['title']}（属于“{chapter}”）
课件和复习提纲里与它有关的内容：
{evidence[:9000]}

考过它的题（节选）：
{questions[:4000]}

格式规范里关于知识点的部分：
{SPEC.split('## 一个知识点')[1].split('## 一门课')[0]}

要求：
- 写学生需要的：它是什么、为什么需要、怎么做、和相近概念的区别、常见的坑，配一个算对了的例子（可以取自上面的题）。
- 讲解可以用一两个问题引导读者自己想到关键点，但不要出现“苏格拉底”“第一性原理”之类的词。
- 用课件里的术语和记号，300～800 字，公式用 LaTeX，必要时用表格。
- 需要分段时用 ## 小标题，小标题不编号（不要写“1.”“3.1”）。
- 只输出正文 Markdown，不要 front matter，不要 # 标题。"""
        body, author = pool.chat("strong", [{"role": "user", "content": prompt}], think=True, max_tokens=5000)
        review = f"""审读《{subject}》知识点“{topic['title']}”的讲解，找出事实或计算错误、与课件术语不一致、含糊不清之处。

{body[:7000]}

只输出 JSON：{{"ok": true/false, "fixes": "需要改的地方，逐条；没有则为空"}}"""
        verdict_text, checker = pool.chat("strong", [{"role": "user", "content": review}], think=True, max_tokens=2000,
                                          avoid=author.split(":")[0])
        verdict = json_of(verdict_text)
        if not verdict.get("ok") and verdict.get("fixes"):
            fix = f"""按审读意见修改这篇讲解。输出修改后的完整全文（没有问题的部分原样保留），只输出正文 Markdown；小标题不编号。

审读意见：
{verdict['fixes']}

原文：
{body}"""
            revised, _ = pool.chat("strong", [{"role": "user", "content": fix}], max_tokens=6000)
            if len(revised) < 0.7 * len(body):
                raise ValueError("the revision returned only part of the note")
            body = revised
        return {"body": re.sub(r"^```(?:markdown)?\s*|\s*```$", "", body.strip()), "author": author, "checker": checker,
                "reviewed": verdict}
    return cached("explain", 2, (subject, topic["id"], topic["title"], evidence[:9000], questions[:4000]), retried(make))
