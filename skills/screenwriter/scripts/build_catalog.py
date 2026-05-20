# -*- coding: utf-8 -*-
"""扫描整个片库,生成 references/library_catalog.md(全库分类目录 + 统计)。
类型为按片名关键词的粗略推测,仅供检索;可靠类型范例见 reference_library_index.md / case_studies.md。
用法: python build_catalog.py
"""
import os, glob, sys, collections
sys.stdout.reconfigure(encoding="utf-8")

ROOT = r"C:\Users\ZHD\Desktop\世界经典电影剧本中外电影经典剧本"
OUT = r"C:\Users\ZHD\.claude\skills\screenwriter\references\library_catalog.md"

GENRE_KW = {
    "恐怖/惊悚": ["鬼", "恐怖", "惊魂", "惊悚", "凶", "咒", "诅咒", "灵异", "僵尸", "怪谈", "午夜", "幽灵", "死神", "招魂", "电锯", "寂静"],
    "爱情": ["爱", "恋", "情", "婚", "暗恋", "初恋", "倾城", "情书", "新娘", "约会", "前任", "失恋"],
    "喜剧": ["喜剧", "搞笑", "囧", "开心", "欢乐", "爆笑", "闹", "疯狂的", "夏洛"],
    "动作/冒险": ["特工", "谍", "枪", "追击", "速度", "碟中谍", "夺宝", "历险", "冒险", "功夫", "拳", "敢死", "战狼"],
    "悬疑/犯罪": ["谋杀", "凶案", "侦探", "推理", "罪", "犯罪", "通缉", "卧底", "盗", "劫", "黑帮", "教父", "唐人街", "记忆碎片", "嫌疑", "毒"],
    "科幻/奇幻": ["星球", "星际", "机器人", "外星", "未来", "时空", "异形", "黑客", "超能", "魔戒", "哈利", "阿凡达", "赛博", "元素", "盗梦", "机械"],
    "战争": ["战争", "大战", "战役", "集结号", "拯救大兵", "南京", "抗战", "八佰", "硫磺岛", "敦刻尔克"],
    "武侠/古装": ["侠", "剑", "刀", "江湖", "武林", "卧虎", "刺客", "绣春", "王朝", "宫", "皇"],
    "历史/传记": ["传记", "总统", "拿破仑", "甘地", "奥本海默", "机长", "传奇", "国王", "女王", "鲁斯丁", "奈德"],
    "动画": ["动画", "总动员", "奇缘", "历险记", "喜羊羊", "哪吒", "大圣", "疯狂动物", "千与千寻", "龙猫"],
}


def guess_genre(name):
    hits = [g for g, kws in GENRE_KW.items() if any(k in name for k in kws)]
    if not hits:
        return "未分类"
    return "/".join(hits[:2])


def pdf_kind(path):
    try:
        import fitz
        d = fitz.open(path)
        n = min(3, d.page_count)
        c = sum(len(d[i].get_text().strip()) for i in range(n))
        d.close()
        return "扫描" if c / max(1, n) < 50 else "文字"
    except Exception:
        return "?"


rows = []
for f in sorted(glob.glob(os.path.join(ROOT, "*"))):
    if os.path.isdir(f):
        continue
    name = os.path.basename(f)
    ext = os.path.splitext(name)[1].lower()
    if ext not in (".pdf", ".docx", ".doc", ".txt", ".html", ".htm"):
        continue
    if ext == ".pdf":
        k = pdf_kind(f)
        method = "PDF·" + ("扫描→OCR" if k == "扫描" else "文字直读")
    elif ext == ".docx":
        method = "docx直读"
    elif ext == ".doc":
        method = ".doc(需转docx)"
    elif ext == ".txt":
        method = "txt直读"
    else:
        method = "html直读"
    rows.append((guess_genre(name), name, method))

# 统计
by_genre = collections.Counter(r[0] for r in rows)
by_method = collections.Counter(r[2].split("·")[0].split("(")[0] for r in rows)

lines = []
lines.append("# 全库目录 — Library Catalog (自动生成)\n")
lines.append(f"片库根目录:`{ROOT}`\n")
lines.append("> 读取任意一部:`python scripts/read_script.py \"<根目录>/<文件名>\"`(扫描件自动 OCR)。")
lines.append("> 下面的「类型」是按**片名关键词的粗略推测**,仅供检索;**可靠的类型范例**见 `reference_library_index.md` 与 `case_studies.md`。\n")
lines.append(f"**总计 {len(rows)} 部**。读取方式分布:" + " · ".join(f"{k} {v}" for k, v in by_method.most_common()) + "\n")
lines.append("类型推测分布:" + " · ".join(f"{k} {v}" for k, v in by_genre.most_common()) + "\n")
lines.append("---\n")

for genre, _ in by_genre.most_common():
    items = sorted([r for r in rows if r[0] == genre], key=lambda x: x[1])
    lines.append(f"## {genre}({len(items)})\n")
    for _, name, method in items:
        lines.append(f"- {name}  `[{method}]`")
    lines.append("")

with open(OUT, "w", encoding="utf-8") as fh:
    fh.write("\n".join(lines))

print("WROTE:", OUT)
print("TOTAL:", len(rows))
print("METHODS:", dict(by_method))
print("GENRES:", dict(by_genre))
