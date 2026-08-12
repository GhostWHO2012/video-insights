from __future__ import annotations

import json
import re
import shutil
import urllib.request
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
VIDEOS_DIR = ROOT / "videos"
DATA_FILE = ROOT / "data" / "episodes.json"
PROJECTS_DIR = Path(r"N:\C\Youtube\downloads\projects")
REPORT_FILE = ROOT / "missing_covers.md"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def norm(text: str) -> str:
    text = (text or "").lower()
    text = text.replace("｜", " ").replace("|", " ").replace("_", " ")
    text = re.sub(r"[^\w\u4e00-\u9fff]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def tokens(text: str) -> set[str]:
    return {t for t in norm(text).split() if len(t) > 1}


def score_image_for_episode(image: Path, episode: dict) -> int:
    hay = tokens(" ".join([image.stem, image.parent.name, image.parent.parent.name]))
    needles = tokens(" ".join([
        episode.get("title", ""),
        episode.get("bilibili_title", ""),
        episode.get("original_title", ""),
        episode.get("folder_title", ""),
    ]))
    score = len(hay & needles) * 10
    joined_hay = norm(" ".join([image.stem, image.parent.name, image.parent.parent.name]))
    for field in ["original_title", "title", "folder_title"]:
        value = norm(episode.get(field, ""))
        if value and (value in joined_hay or joined_hay in value):
            score += 80
    return score


def save_jpeg(src: Path, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    try:
        with Image.open(src) as image:
            image = image.convert("RGB")
            image.save(dest, "JPEG", quality=88, optimize=True)
    except Exception:
        shutil.copy2(src, dest)


def youtube_id(url: str) -> str:
    if not url:
        return ""
    patterns = [
        r"[?&]v=([^&]+)",
        r"youtu\.be/([^?&/]+)",
        r"youtube\.com/embed/([^?&/]+)",
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return ""


def download_youtube_cover(video_id: str, dest: Path) -> bool:
    if not video_id:
        return False
    urls = [
        f"https://i.ytimg.com/vi/{video_id}/maxresdefault.jpg",
        f"https://i.ytimg.com/vi/{video_id}/hqdefault.jpg",
    ]
    for url in urls:
        try:
            with urllib.request.urlopen(url, timeout=20) as response:
                data = response.read()
            if len(data) < 5000:
                continue
            dest.write_bytes(data)
            return True
        except Exception:
            continue
    return False


def main() -> None:
    episodes = read_json(DATA_FILE)
    exts = {".jpg", ".jpeg", ".png", ".webp"}
    images = [p for p in PROJECTS_DIR.rglob("*") if p.is_file() and p.suffix.lower() in exts]
    copied = []
    downloaded = []
    missing = []

    for episode in episodes:
        video_dir = ROOT / episode["path"]
        cover = video_dir / "cover.jpeg"
        if cover.exists():
            continue

        candidates = sorted(((score_image_for_episode(img, episode), img) for img in images), reverse=True)
        best_score, best_img = candidates[0] if candidates else (0, None)
        if best_img and best_score >= 60:
            save_jpeg(best_img, cover)
            copied.append((episode.get("bilibili_title") or episode.get("title"), best_img, best_score))
            continue

        vid = youtube_id(episode.get("youtube_url", ""))
        if download_youtube_cover(vid, cover):
            downloaded.append((episode.get("bilibili_title") or episode.get("title"), vid))
        else:
            missing.append(episode)

    report = ["# Missing covers", ""]
    report.append(f"- local copied: {len(copied)}")
    report.append(f"- youtube downloaded: {len(downloaded)}")
    report.append(f"- still missing: {len(missing)}")
    report.append("")
    if missing:
        report.append("## Still missing")
        for episode in missing:
            report.append(f"- {episode.get('bilibili_title') or episode.get('title')} | {episode.get('youtube_url') or episode.get('bilibili_url') or ''} | {episode.get('path')}")
    REPORT_FILE.write_text("\n".join(report), encoding="utf-8")
    print(f"local copied {len(copied)}")
    print(f"youtube downloaded {len(downloaded)}")
    print(f"still missing {len(missing)}")
    for title, img, score in copied[:20]:
        print("copied", score, title, "<=", img)
    for title, vid in downloaded[:20]:
        print("downloaded", title, vid)


if __name__ == "__main__":
    main()
