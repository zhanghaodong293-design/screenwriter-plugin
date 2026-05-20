# -*- coding: utf-8 -*-
"""通用剧本读取器 —— 把片库内任意格式的剧本抽成纯文本到 stdout。

用法:
    python read_script.py "<文件路径>" [--max N] [--ocr-pages N]

支持:
    .txt / .html / .htm   直读
    .docx                 python-docx
    .pdf                  文字版用 PyMuPDF 直抽;扫描版自动走 rapidocr OCR(中英文)
    .doc                  旧二进制格式,提示转 .docx

依赖(均已装):pymupdf, rapidocr-onnxruntime, python-docx
"""
import sys, os, re, argparse


def read_txt(p):
    return open(p, encoding="utf-8", errors="replace").read()


def read_html(p):
    html = open(p, encoding="utf-8", errors="replace").read()
    html = re.sub(r"(?is)<(script|style).*?</\1>", "", html)
    return re.sub(r"<[^>]+>", "", html)


def read_docx(p):
    import docx
    d = docx.Document(p)
    return "\n".join(par.text for par in d.paragraphs)


def read_pdf(p, ocr_pages=0):
    import fitz
    d = fitz.open(p)
    txt = "".join(pg.get_text() for pg in d)
    if len(txt.strip()) > 200:
        return txt  # 文字版,直接返回
    # 扫描版 —— 渲染每页为图片再 OCR
    from rapidocr_onnxruntime import RapidOCR
    ocr = RapidOCR()
    n = d.page_count if ocr_pages <= 0 else min(ocr_pages, d.page_count)
    out = []
    for i in range(n):
        pix = d[i].get_pixmap(dpi=200)
        res, _ = ocr(pix.tobytes("png"))
        if res:
            out.append("\n".join(line[1] for line in res))
    return "\n".join(out)


def extract(path, ocr_pages=0):
    ext = os.path.splitext(path)[1].lower()
    if ext == ".txt":
        return read_txt(path)
    if ext in (".html", ".htm"):
        return read_html(path)
    if ext == ".docx":
        return read_docx(path)
    if ext == ".pdf":
        return read_pdf(path, ocr_pages)
    if ext == ".doc":
        return "(.doc 旧格式不支持,请先另存为 .docx)"
    return "(不支持的格式: %s)" % ext


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="通用剧本读取器")
    ap.add_argument("path", help="剧本文件路径")
    ap.add_argument("--max", type=int, default=0, help="最多输出字符数(0=全部)")
    ap.add_argument("--ocr-pages", type=int, default=0, help="扫描件最多 OCR 页数(0=全部)")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    t = extract(a.path, a.ocr_pages)
    if a.max > 0:
        t = t[:a.max]
    sys.stdout.write(t)
