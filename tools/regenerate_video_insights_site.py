from __future__ import annotations

import html
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VIDEOS_DIR = ROOT / "videos"
DATA_FILE = ROOT / "data" / "episodes.json"


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8-sig", errors="ignore")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def esc(value: object) -> str:
    return html.escape("" if value is None else str(value), quote=True)


def rel(path: Path, base: Path) -> str:
    return path.relative_to(base).as_posix()


def clean_date(value: str) -> str:
    cleaned = (value or "").replace("发布时间:", "").strip()
    return "" if cleaned in {"待补充", "-", "无"} else cleaned


def date_sort_value(value: str) -> str:
    cleaned = clean_date(value)
    match = re.search(r"(\d{4})[-/.年](\d{1,2})[-/.月](\d{1,2})(?:[ 日T]+(\d{1,2}):(\d{1,2})(?::(\d{1,2}))?)?", cleaned)
    if not match:
        return "00000000000000"
    y, m, d, hh, mm, ss = match.groups()
    return f"{int(y):04d}{int(m):02d}{int(d):02d}{int(hh or 0):02d}{int(mm or 0):02d}{int(ss or 0):02d}"


def duration_seconds(value: str) -> int:
    parts = [p for p in re.split(r"[:：]", value or "") if p.strip().isdigit()]
    if not parts:
        return 0
    nums = [int(p) for p in parts]
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return nums[0] * 60 + nums[1]
    return nums[-3] * 3600 + nums[-2] * 60 + nums[-1]


def natural_key(path: Path):
    return [int(x) if x.isdigit() else x.lower() for x in re.split(r"(\d+)", path.name)]


def discover_subtitles(video_dir: Path) -> list[Path]:
    sub_dir = video_dir / "subtitles"
    if not sub_dir.exists():
        return []
    return sorted(sub_dir.glob("*.srt"), key=lambda p: p.stat().st_mtime, reverse=True)


def subtitle_score(path: Path) -> tuple[int, float]:
    name = path.name.lower()
    score = 0
    for token, weight in [
        ("中文在上", 90),
        ("双语", 60),
        ("有翻译参考资料版", 40),
        ("参考", 30),
        ("英文术语", 35),
        ("asr", 25),
        ("校正", 25),
        ("小修", 25),
        ("去多余", 35),
        ("标点", 20),
        ("opus4", 12),
        ("opus4-8", 14),
        ("final", 12),
        ("raw", -80),
        ("英文原版", -70),
        ("split_en", -60),
        ("中文章", -30),
    ]:
        if token in name:
            score += weight
    return score, path.stat().st_mtime


def best_subtitle(subtitles: list[Path]) -> Path | None:
    if not subtitles:
        return None
    return sorted(subtitles, key=subtitle_score, reverse=True)[0]


def discover_outlines(video_dir: Path) -> list[Path]:
    out_dir = video_dir / "outlines"
    if not out_dir.exists():
        return []
    exts = {".png", ".jpg", ".jpeg", ".webp"}
    return sorted([p for p in out_dir.iterdir() if p.suffix.lower() in exts], key=natural_key)


def parse_srt(path: Path, limit: int | None = None) -> list[dict[str, object]]:
    text = read_text(path).replace("\ufeff", "").strip()
    if not text:
        return []
    blocks = re.split(r"\n\s*\n", text)
    items = []
    for block in blocks:
        lines = [line.strip() for line in block.splitlines() if line.strip()]
        if len(lines) < 2:
            continue
        idx = lines[0] if lines[0].isdigit() else str(len(items) + 1)
        time_line_index = 1 if "-->" in lines[1] else 0
        if "-->" not in lines[time_line_index]:
            continue
        time_line = lines[time_line_index]
        content = lines[time_line_index + 1 :]
        zh, en, other = [], [], []
        for line in content:
            if re.search(r"[\u4e00-\u9fff]", line):
                zh.append(line)
            elif re.search(r"[A-Za-z]", line):
                en.append(line)
            else:
                other.append(line)
        items.append({"index": idx, "time": time_line, "zh": zh, "en": en, "other": other})
        if limit and len(items) >= limit:
            break
    return items


def md_to_html(md: str) -> str:
    lines = md.splitlines()
    out: list[str] = []
    in_list = False
    for raw in lines:
        line = raw.rstrip()
        if not line:
            if in_list:
                out.append("</ul>")
                in_list = False
            continue
        if line.startswith("### "):
            if in_list:
                out.append("</ul>")
                in_list = False
            out.append(f"<h3>{esc(line[4:])}</h3>")
        elif line.startswith("## "):
            if in_list:
                out.append("</ul>")
                in_list = False
            out.append(f"<h2>{esc(line[3:])}</h2>")
        elif line.startswith("# "):
            if in_list:
                out.append("</ul>")
                in_list = False
            out.append(f"<h1>{esc(line[2:])}</h1>")
        elif re.match(r"^\s*[-*]\s+", line):
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append(f"<li>{linkify(esc(re.sub(r'^\\s*[-*]\\s+', '', line)))}</li>")
        else:
            if in_list:
                out.append("</ul>")
                in_list = False
            out.append(f"<p>{linkify(esc(line))}</p>")
    if in_list:
        out.append("</ul>")
    return "\n".join(out)


def linkify(text: str) -> str:
    return re.sub(
        r"(https?://[^\s<]+)",
        lambda m: f'<a href="{m.group(1)}">{m.group(1)}</a>',
        text,
    )


SITE_CSS = """
:root{--bg:#0a192f;--ink:#ccd6f6;--muted:#8892b0;--line:#233554;--card:#112240;--brand:#64ffda;--brand2:#7dd3fc;--soft:rgba(100,255,218,.08);--shadow:0 20px 55px rgba(2,12,27,.45)}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Microsoft YaHei",Arial,sans-serif;line-height:1.65}.wrap{width:min(1180px,calc(100% - 36px));margin:0 auto}.topbar{position:sticky;top:0;z-index:20;background:rgba(10,25,47,.86);border-bottom:1px solid var(--line);backdrop-filter:blur(14px)}.topbar .wrap{display:flex;align-items:center;justify-content:space-between;padding:14px 0}.brand{font-weight:800;letter-spacing:.2px;color:var(--ink);text-decoration:none}.nav{display:flex;gap:14px;align-items:center}.nav a{color:var(--muted);text-decoration:none;font-size:14px}.hero{padding:42px 0 22px}.eyebrow{color:var(--brand);font-weight:700;font-size:14px}.hero h1{font-size:42px;line-height:1.12;margin:10px 0 12px;letter-spacing:0}.hero p{font-size:17px;color:var(--muted);max-width:780px}.stats{display:flex;gap:10px;flex-wrap:wrap;margin-top:18px}.chip{display:inline-flex;align-items:center;gap:6px;border:1px solid var(--line);background:rgba(17,34,64,.78);border-radius:999px;padding:8px 12px;color:var(--muted);font-size:13px}.toolbar{display:grid;grid-template-columns:1fr 220px auto;gap:12px;margin:22px 0}.search,.sort{height:44px;border:1px solid var(--line);border-radius:10px;padding:0 14px;font-size:15px;background:#020c1b;color:var(--ink)}.search::placeholder{color:#66799f}.sort{color:var(--ink)}.grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px;margin:18px 0 42px}.card{display:flex;flex-direction:column;min-height:100%;background:var(--card);border:1px solid rgba(35,53,84,.95);border-radius:14px;overflow:hidden;text-decoration:none;color:inherit;box-shadow:0 2px 8px rgba(2,12,27,.22);transition:.18s ease}.card:hover{transform:translateY(-3px);box-shadow:var(--shadow);border-color:rgba(100,255,218,.55)}.cover{aspect-ratio:16/9;background:linear-gradient(135deg,#020c1b,#1d4ed8);display:flex;align-items:center;justify-content:center;color:var(--ink);font-size:18px;font-weight:800;text-align:center;padding:24px;overflow:hidden}.cover img{width:100%;height:100%;object-fit:cover;display:block}.card-body{padding:16px}.date{font-size:13px;color:var(--muted);margin-bottom:8px}.title{font-size:18px;font-weight:800;line-height:1.35;margin-bottom:8px;color:#e6f1ff}.original{font-size:13px;color:var(--muted);line-height:1.45;margin-bottom:10px}.meta{display:flex;gap:8px;flex-wrap:wrap;margin:10px 0}.pill{font-size:12px;color:#a8b2d1;background:rgba(2,12,27,.42);border:1px solid var(--line);border-radius:999px;padding:3px 8px}.links{display:flex;gap:10px;flex-wrap:wrap;margin-top:auto;padding-top:8px}.links span,.btn{color:var(--brand);font-weight:700;font-size:14px}.episode-hero{padding:34px 0 22px}.episode-grid{display:grid;grid-template-columns:1.3fr .7fr;gap:22px;align-items:start}.panel{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:20px;box-shadow:0 2px 8px rgba(2,12,27,.22)}.episode-title{font-size:34px;line-height:1.2;margin:10px 0;color:#e6f1ff}.resource-grid{display:flex;gap:10px;flex-wrap:wrap;margin-top:18px}.resource-grid a{display:inline-flex;align-items:center;border:1px solid rgba(100,255,218,.35);background:var(--soft);color:var(--brand);padding:9px 12px;border-radius:10px;text-decoration:none;font-weight:700;font-size:14px}.cover-large{border-radius:16px;overflow:hidden;background:linear-gradient(135deg,#020c1b,#164e63);aspect-ratio:16/9;color:var(--ink);display:flex;align-items:center;justify-content:center;text-align:center;padding:28px;font-weight:800}.cover-large img{width:100%;height:100%;object-fit:cover}.section{margin:24px 0}.section h2{font-size:24px;margin:0 0 12px;color:#e6f1ff}.outline-row{display:flex;gap:14px;overflow-x:auto;padding:4px 0 12px;scroll-snap-type:x proximity}.outline-card{flex:0 0 280px;background:var(--card);border:1px solid var(--line);border-radius:12px;overflow:hidden;text-decoration:none;color:inherit;scroll-snap-align:start}.outline-card img{width:100%;height:170px;object-fit:cover;display:block}.outline-card span{display:block;padding:10px;font-weight:700;font-size:14px;color:#e6f1ff}.transcript{display:grid;gap:10px}.cue{display:grid;grid-template-columns:116px 1fr;gap:12px;padding:14px;border:1px solid var(--line);border-radius:12px;background:var(--card)}.time{font-family:ui-monospace,SFMono-Regular,Consolas,monospace;color:var(--brand);font-size:13px}.zh{font-size:16px;font-weight:650;color:#e6f1ff}.en{font-size:14px;color:var(--muted);margin-top:3px}.doc{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:22px}.doc h1,.doc h2{margin-top:0;color:#e6f1ff}.doc a{color:var(--brand)}.empty{color:var(--muted);background:rgba(17,34,64,.78);border:1px dashed var(--line);border-radius:12px;padding:18px}.footer{border-top:1px solid var(--line);color:var(--muted);font-size:13px;padding:28px 0;margin-top:38px}@media(max-width:900px){.grid{grid-template-columns:1fr 1fr}.episode-grid{grid-template-columns:1fr}.hero h1{font-size:34px}}@media(max-width:620px){.wrap{width:min(100% - 24px,1180px)}.grid{grid-template-columns:1fr}.toolbar{grid-template-columns:1fr}.cue{grid-template-columns:1fr}.episode-title{font-size:28px}.topbar .wrap{align-items:flex-start;gap:10px;flex-direction:column}}
"""


def page_shell(title: str, body: str, depth: int = 0) -> str:
    prefix = "../" * depth
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} - Video Insights</title>
<style>{SITE_CSS}</style>
</head>
<body>
<header class="topbar"><div class="wrap"><a class="brand" href="{prefix}index.html">Video Insights</a><nav class="nav"><a href="{prefix}index.html">首页</a><a href="{prefix}index.html#episodes">全部视频</a></nav></div></header>
{body}
<footer class="footer"><div class="wrap">AI video subtitles, insights, timelines and references.</div></footer>
</body>
</html>"""


def episode_body(video_dir: Path, meta: dict, subtitle: Path | None, outlines: list[Path]) -> str:
    title = meta.get("bilibili_title") or meta.get("title") or video_dir.name
    original = meta.get("original_title") or ""
    cover = video_dir / "cover.jpeg"
    if cover.exists():
        cover_html = f'<div class="cover-large"><img src="{rel(cover, video_dir)}" alt="{esc(title)}"></div>'
    else:
        cover_html = f'<div class="cover-large">{esc(title)}</div>'
    resources = []
    for label, key in [("B站", "bilibili_url"), ("原视频", "youtube_url")]:
        if meta.get(key):
            resources.append(f'<a href="{esc(meta[key])}">{label}</a>')
    if subtitle:
        resources.append(f'<a href="subtitles/{esc(subtitle.name)}">字幕下载</a>')
    if outlines:
        resources.append('<a href="outlines/index.html">提纲图</a>')
    if (video_dir / "timeline.md").exists() or (video_dir / "timeline.html").exists():
        resources.append('<a href="timeline.html">时间轴</a>')
    if (video_dir / "bilibili.md").exists():
        resources.append('<a href="bilibili.md">B站简介</a>')
    resource_html = "\n".join(resources) or '<span class="pill">资源待补充</span>'
    speakers = meta.get("speakers") or []
    if isinstance(speakers, str):
        speakers = [speakers]
    meta_bits = [
        ("发布日期", clean_date(meta.get("published_at", "")) or "待补充"),
        ("时长", meta.get("duration") or "待补充"),
        ("嘉宾", "、".join(speakers) if speakers else "待补充"),
        ("频道", meta.get("up") or "待补充"),
    ]
    meta_html = "".join(f'<span class="pill">{esc(k)}：{esc(v)}</span>' for k, v in meta_bits)
    outline_html = ""
    if outlines:
        cards = []
        for image in outlines:
            cards.append(f'<a class="outline-card" href="outlines/{esc(image.name)}"><img src="outlines/{esc(image.name)}" alt="{esc(image.stem)}"><span>{esc(image.stem)}</span></a>')
        outline_html = f'<section class="section"><h2>速览图</h2><div class="outline-row">{"".join(cards)}</div></section>'
    else:
        outline_html = '<section class="section"><h2>速览图</h2><div class="empty">暂无提纲图</div></section>'
    if subtitle:
        cues = parse_srt(subtitle)
        rows = []
        for cue in cues:
            zh = "<br>".join(esc(x) for x in cue["zh"])
            en = "<br>".join(esc(x) for x in cue["en"])
            other = "<br>".join(esc(x) for x in cue["other"])
            body = f'<div class="zh">{zh or other}</div>'
            if en:
                body += f'<div class="en">{en}</div>'
            rows.append(f'<article class="cue"><div class="time">{esc(cue["time"])}</div><div>{body}</div></article>')
        transcript_html = f'<section class="section"><h2>文字稿</h2><div class="transcript">{"".join(rows)}</div></section>'
    else:
        transcript_html = '<section class="section"><h2>文字稿</h2><div class="empty">暂未匹配到中文在上字幕，后续补齐后会直接显示在这里。</div></section>'
    return f"""
<main>
  <section class="episode-hero">
    <div class="wrap episode-grid">
      <div class="panel">
        <a class="btn" href="../../index.html">返回目录</a>
        <div class="eyebrow">资源与元信息</div>
        <h1 class="episode-title">{esc(title)}</h1>
        <p class="original">原标题：{esc(original or "待补充")}</p>
        <div class="meta">{meta_html}</div>
        <div class="resource-grid">{resource_html}</div>
      </div>
      {cover_html}
    </div>
  </section>
  <div class="wrap">
    {outline_html}
    {transcript_html}
  </div>
</main>
"""


def subtitles_index(video_dir: Path, meta: dict, subtitles: list[Path], preferred: Path | None) -> str:
    title = meta.get("bilibili_title") or meta.get("title") or video_dir.name
    visible = []
    if preferred:
        visible.append(preferred)
    # Keep every existing file available, but keep the best version first and preserve filenames.
    for sub in sorted(subtitles, key=lambda p: p.name.lower()):
        if sub not in visible:
            visible.append(sub)
    items = "\n".join(
        f'<li><a href="{esc(sub.name)}">{esc(sub.name)}</a>{" <strong>推荐</strong>" if sub == preferred else ""}</li>'
        for sub in visible
    ) or "<li>暂无字幕</li>"
    body = f'<main class="wrap section"><a class="btn" href="../index.html">返回本期</a><div class="doc"><h1>字幕下载</h1><p>{esc(title)}</p><ul>{items}</ul></div></main>'
    return page_shell(f"{title} 字幕下载", body, depth=3)


def outlines_index(video_dir: Path, meta: dict, outlines: list[Path]) -> str:
    title = meta.get("bilibili_title") or meta.get("title") or video_dir.name
    if outlines:
        cards = "".join(f'<a class="outline-card" href="{esc(img.name)}"><img src="{esc(img.name)}" alt="{esc(img.stem)}"><span>{esc(img.name)}</span></a>' for img in outlines)
        content = f'<div class="outline-row">{cards}</div>'
    else:
        content = '<div class="empty">暂无提纲图</div>'
    body = f'<main class="wrap section"><a class="btn" href="../index.html">返回本期</a><div class="doc"><h1>提纲图</h1><p>{esc(title)}</p>{content}</div></main>'
    return page_shell(f"{title} 提纲图", body, depth=3)


def timeline_page(video_dir: Path, meta: dict) -> str:
    title = meta.get("bilibili_title") or meta.get("title") or video_dir.name
    timeline = video_dir / "timeline.md"
    if timeline.exists():
        content = md_to_html(read_text(timeline))
    else:
        content = '<div class="empty">暂无时间轴</div>'
    body = f'<main class="wrap section"><a class="btn" href="index.html">返回本期</a><div class="doc"><h1>时间轴</h1>{content}</div></main>'
    return page_shell(f"{title} 时间轴", body, depth=2)


def build_home(episodes: list[dict]) -> str:
    cards = []
    for ep in episodes:
        path = ep.get("path", "")
        title = ep.get("bilibili_title") or ep.get("title") or Path(path).name
        cover = ep.get("cover")
        cover_html = f'<img src="{esc(path + cover)}" alt="{esc(title)}">' if cover else esc(title)
        speakers = ep.get("speakers") or []
        if isinstance(speakers, str):
            speakers = [speakers]
        speaker_text = "、".join(speakers[:3]) if speakers else "嘉宾待补充"
        cards.append(f"""
<a class="card" href="{esc(path)}" data-date="{date_sort_value(ep.get("published_at", ""))}" data-title="{esc(title.lower())}" data-duration="{duration_seconds(str(ep.get("duration") or ""))}">
  <div class="cover">{cover_html}</div>
  <div class="card-body">
    <div class="date">发布时间：{esc(clean_date(ep.get("published_at", "")) or "待补充")}</div>
    <div class="title">{esc(title)}</div>
    <div class="original">原题：{esc(ep.get("original_title") or "待补充")}</div>
    <div class="meta"><span class="pill">{esc(speaker_text)}</span><span class="pill">{esc(ep.get("duration") or "时长待补充")}</span><span class="pill">字幕 {esc(ep.get("subtitle_count", 0))}</span><span class="pill">提纲图 {esc(ep.get("outline_count", 0))}</span></div>
    <div class="links"><span>资源</span><span>字幕</span><span>时间轴</span><span>提纲图</span></div>
  </div>
</a>""")
    body = f"""
<main>
  <section class="hero"><div class="wrap">
    <div class="eyebrow">公开视频内容合集</div>
    <h1>AI 视频字幕、洞见目录与资料库</h1>
    <p>每一期集中保存原视频链接、B站简介、中文字幕稿、时间轴、提纲图和补充资料。点开任意卡片即可浏览资源和网页文字稿。</p>
    <div class="stats"><span class="chip">共 {len(episodes)} 期</span><span class="chip">字幕与提纲集中管理</span><span class="chip">GitHub Pages 自动发布</span></div>
    <div class="toolbar"><input class="search" id="q" placeholder="搜索标题、嘉宾、主题"><select class="sort" id="sort"><option value="date-desc">发布时间：最新在上</option><option value="date-asc">发布时间：最早在上</option><option value="title-asc">名称：A-Z</option><option value="title-desc">名称：Z-A</option><option value="duration-desc">时长：最长在上</option><option value="duration-asc">时长：最短在上</option></select><span class="chip">整张卡片可点击</span></div>
  </div></section>
  <section class="wrap" id="episodes"><div class="grid" id="grid">{"".join(cards)}</div></section>
</main>
<script>
const q=document.getElementById('q');const sort=document.getElementById('sort');const grid=document.getElementById('grid');let cards=[...grid.children];
function apply(){{const s=q.value.trim().toLowerCase();const mode=sort.value;cards.sort((a,b)=>{{if(mode==='date-desc')return b.dataset.date.localeCompare(a.dataset.date);if(mode==='date-asc')return a.dataset.date.localeCompare(b.dataset.date);if(mode==='title-asc')return a.dataset.title.localeCompare(b.dataset.title,'zh-Hans-CN');if(mode==='title-desc')return b.dataset.title.localeCompare(a.dataset.title,'zh-Hans-CN');if(mode==='duration-desc')return Number(b.dataset.duration)-Number(a.dataset.duration);if(mode==='duration-asc')return Number(a.dataset.duration)-Number(b.dataset.duration);return 0;}});cards.forEach(c=>{{c.style.display=c.innerText.toLowerCase().includes(s)?'flex':'none';grid.appendChild(c);}});}}
q.addEventListener('input',apply);sort.addEventListener('change',apply);apply();
</script>
"""
    return page_shell("Video Insights", body, depth=0)


def main() -> None:
    episodes = json.loads(read_text(DATA_FILE)) if DATA_FILE.exists() else []
    by_path = {e.get("path", "").strip("/"): e for e in episodes if e.get("path")}
    rebuilt: list[dict] = []
    for video_dir in sorted([p for p in VIDEOS_DIR.iterdir() if p.is_dir()], key=natural_key):
        meta_path = video_dir / "meta.json"
        meta = json.loads(read_text(meta_path)) if meta_path.exists() else {}
        key = f"videos/{video_dir.name}"
        meta.update(by_path.get(key, {}))
        meta["path"] = f"videos/{video_dir.name}/"
        meta["slug"] = video_dir.name
        cover = video_dir / "cover.jpeg"
        if cover.exists():
            meta["cover"] = "cover.jpeg"
        else:
            meta.pop("cover", None)
        outlines = discover_outlines(video_dir)
        subtitles = discover_subtitles(video_dir)
        preferred = best_subtitle(subtitles)
        meta["outline_count"] = len(outlines)
        meta["subtitle_count"] = len(subtitles)
        meta["outline_files"] = [p.name for p in outlines]
        if preferred:
            meta["subtitle_file"] = preferred.name
        write_text(meta_path, json.dumps(meta, ensure_ascii=False, indent=2))
        write_text(video_dir / "index.html", page_shell(str(meta.get("bilibili_title") or meta.get("title") or video_dir.name), episode_body(video_dir, meta, preferred, outlines), depth=2))
        write_text(video_dir / "subtitles" / "index.html", subtitles_index(video_dir, meta, subtitles, preferred))
        write_text(video_dir / "outlines" / "index.html", outlines_index(video_dir, meta, outlines))
        write_text(video_dir / "timeline.html", timeline_page(video_dir, meta))
        rebuilt.append(meta)
    def episode_sort_key(item: dict) -> tuple[str, str]:
        date = clean_date(item.get("published_at", ""))
        slug = item.get("slug") or ""
        match = re.search(r"(\d+)", slug)
        number = f"{int(match.group(1)):04d}" if match else "0000"
        return date or number, number

    rebuilt.sort(key=episode_sort_key, reverse=True)
    write_text(DATA_FILE, json.dumps(rebuilt, ensure_ascii=False, indent=2))
    write_text(ROOT / "index.html", build_home(rebuilt))
    print(f"rebuilt {len(rebuilt)} episodes")
    print(f"with covers {sum(1 for e in rebuilt if e.get('cover'))}")
    print(f"with subtitles {sum(1 for e in rebuilt if e.get('subtitle_count'))}")
    print(f"with outlines {sum(1 for e in rebuilt if e.get('outline_count'))}")


if __name__ == "__main__":
    main()
