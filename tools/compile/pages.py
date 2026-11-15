"""Steps 0–1: a source file becomes pages, each the Markdown MinerU read from it, with its figures cut out.

Word and PowerPoint files are exported to PDF by Office itself, so drawings and layout survive. Every PDF is read by
MinerU (layout, text, formulas, tables, figures), the four accounts in turn, longer files in parts of 150 pages. Page
images are rendered too, so a page can be looked at again; images are pages of their own, plain text is one page.
"""
from __future__ import annotations

import io
import itertools
import json
import os
import subprocess
import threading
import time
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path

import pymupdf

from .store import PAGES, WORK, cached

OFFICE = {".doc": "Word", ".docx": "Word", ".ppt": "PowerPoint", ".pptx": "PowerPoint"}
IMAGES = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".webp"}
DPI = 110
VERSION = 2


def _office_pdf(path: Path, sha: str) -> Path:
    out = WORK / "pdf" / f"{sha}.pdf"
    if out.exists():
        return out
    out.parent.mkdir(parents=True, exist_ok=True)
    app = OFFICE[path.suffix.lower()]
    script = (f"$a = New-Object -ComObject Word.Application; $a.Visible = $false; $d = $a.Documents.Open('{path}', $false, $true); "
              f"$d.ExportAsFixedFormat('{out}', 17); $d.Close(0); $a.Quit()" if app == "Word" else
              f"$a = New-Object -ComObject PowerPoint.Application; $p = $a.Presentations.Open('{path}', $true, $false, $false); "
              f"$p.SaveAs('{out}', 32); $p.Close(); $a.Quit()")
    result = subprocess.run(["pwsh", "-NoProfile", "-Command", script], capture_output=True, text=True, timeout=600)
    if not out.exists():
        raise RuntimeError(f"Office could not export {path.name}: {result.stderr[-300:]}")
    return out


def _render(pdf: Path, sha: str) -> list[dict]:
    pages = []
    folder = PAGES / sha
    folder.mkdir(parents=True, exist_ok=True)
    with pymupdf.open(pdf) as document:
        for number, page in enumerate(document, start=1):
            image = folder / f"{number:03}.jpg"
            if not image.exists():
                page.get_pixmap(dpi=DPI).save(image, jpg_quality=82)
            text = page.get_text("text").strip()
            pages.append({"number": number, "image": str(image), "text": text, "reader": "text-layer"})
    return pages


class MinerU:
    """Every MinerU account given (MINERU_TOKEN, MINERU_TOKEN_2, …), each used in turn."""
    tokens = [os.environ[name] for name in sorted(os.environ, key=lambda n: (len(n), n)) if name.startswith("MINERU_TOKEN")]
    turn = itertools.cycle(range(len(tokens)))
    lock = threading.Lock()
    spent: set[int] = set()

    @classmethod
    def read(cls, pdf: Path) -> list[str]:
        """The Markdown of every page of a PDF, by page."""
        for _ in range(8):
            with cls.lock:
                live = [i for i in range(len(cls.tokens)) if i not in cls.spent]
                if not live:
                    raise RuntimeError("every MinerU account is out of quota")
                index = next(i for i in cls.turn if i in live)
            try:
                return cls._read(pdf, cls.tokens[index])
            except PermissionError:
                cls.spent.add(index)
        raise RuntimeError(f"MinerU could not read {pdf.name}")

    @staticmethod
    def _call(token: str, method: str, path: str, body: dict | None = None) -> dict:
        request = urllib.request.Request(f"https://mineru.net/api/v4{path}", method=method,
                                         data=json.dumps(body).encode() if body else None,
                                         headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"})
        with urllib.request.urlopen(request, timeout=120) as response:
            answer = json.load(response)
        if answer.get("code") != 0:
            if "quota" in str(answer).lower() or "额度" in str(answer):
                raise PermissionError(str(answer))
            raise RuntimeError(f"MinerU {path}: {answer}")
        return answer["data"]

    @classmethod
    def _read(cls, pdf: Path, token: str) -> list[str]:
        data = cls._call(token, "POST", "/file-urls/batch", {"files": [{"name": pdf.name, "data_id": pdf.stem}],
                                                              "model_version": "vlm", "language": "ch"})
        url = urllib.parse.urlsplit(data["file_urls"][0])
        import http.client
        connection = http.client.HTTPSConnection(url.netloc, timeout=600)
        body = pdf.read_bytes()
        connection.putrequest("PUT", f"{url.path}?{url.query}", skip_accept_encoding=True)
        connection.putheader("Content-Length", str(len(body)))
        connection.endheaders()
        connection.send(body)
        if connection.getresponse().status != 200:
            raise RuntimeError(f"MinerU upload of {pdf.name} failed")
        for _ in range(360):
            time.sleep(10)
            result = cls._call(token, "GET", f"/extract-results/batch/{data['batch_id']}")["extract_result"][0]
            if result["state"] == "failed":
                raise RuntimeError(f"MinerU failed on {pdf.name}: {result.get('err_msg')}")
            if result["state"] == "done":
                archive = zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(result["full_zip_url"], timeout=600).read()))
                return cls._pages(archive, pdf)
        raise RuntimeError(f"MinerU took too long on {pdf.name}")

    @staticmethod
    def _pages(archive: zipfile.ZipFile, pdf: Path) -> list[str]:
        listing = next(name for name in archive.namelist() if name.endswith("_content_list.json"))
        figures = FIGURES / pdf.stem
        by_page: dict[int, list[str]] = {}
        for block in json.loads(archive.read(listing)):
            text = _block_markdown(block, figures, archive)
            if text.strip():
                by_page.setdefault(int(block.get("page_idx", 0)), []).append(text)
        count = 1 + max(by_page, default=0)
        return ["\n\n".join(by_page.get(i, [])) for i in range(count)]


FIGURES = WORK / "figures"


def _block_markdown(block: dict, figures: Path, archive: zipfile.ZipFile) -> str:
    kind = block.get("type")
    if kind == "text":
        level = int(block.get("text_level") or 0)
        return ("#" * min(level + 1, 4) + " " if level else "") + block.get("text", "")
    if kind == "equation":
        return block.get("text") or (f"$$\n{block['latex']}\n$$" if block.get("latex") else "")
    if kind == "table":
        caption = " ".join(block.get("table_caption") or [])
        return "\n".join(part for part in (caption, block.get("table_body", ""), " ".join(block.get("table_footnote") or [])) if part)
    if kind == "image" and block.get("img_path"):
        name = Path(block["img_path"]).name
        target = figures / name
        if not target.exists():
            figures.mkdir(parents=True, exist_ok=True)
            target.write_bytes(archive.read(next(n for n in archive.namelist() if n.endswith(block["img_path"]))))
        caption = " ".join(block.get("image_caption") or block.get("img_caption") or [])
        return f"![{caption}](figure:{figures.name}/{name})"
    return block.get("text", "")


def pages_of(path: Path, sha: str) -> list[dict]:
    """Every page of a source file as MinerU read it, beside its rendered image."""
    def make():
        suffix = path.suffix.lower()
        if suffix in (".txt", ".md"):
            return [{"number": 1, "image": None, "markdown": path.read_text(encoding="utf-8", errors="replace")}]
        if suffix in IMAGES:
            pdf = WORK / "pdf" / f"{sha}.pdf"
            if not pdf.exists():
                pdf.parent.mkdir(parents=True, exist_ok=True)
                with pymupdf.open(path) as image:
                    pymupdf.open("pdf", image.convert_to_pdf()).save(pdf)
        else:
            pdf = _office_pdf(path, sha) if suffix in OFFICE else path
        pages = _render(pdf, sha)
        texts: list[str] = []
        with pymupdf.open(pdf) as document:
            for start in range(0, len(document), 150):
                part = WORK / "pdf" / f"{sha}-{start // 150}.pdf"
                if not part.exists():
                    piece = pymupdf.open()
                    piece.insert_pdf(document, from_page=start, to_page=min(start + 149, len(document) - 1))
                    piece.save(part)
                texts += MinerU.read(part)
        for page in pages:
            page["markdown"] = texts[page["number"] - 1] if page["number"] - 1 < len(texts) else ""
            del page["text"], page["reader"]
        return pages
    return cached("pages", VERSION, (sha,), make)
