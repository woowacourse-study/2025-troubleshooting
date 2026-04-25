#!/usr/bin/env python3
"""
data/weeks.yml + templates/readme_header.md 로 README.md 전체를 재생성한다.

규칙
- 헤더 파일 아래에 "## 📣 목차" 테이블을 자동 생성
- 주차별 섹션(<a id="week-N"></a>)을 발표자 수에 맞게 2-column table 로 렌더
- PDF / 썸네일 / 유튜브 링크는 weeks.yml 값을 그대로 사용
- 로컬 경로(`thumbnails/...`, `NN_N주차/...`) 는 GitHub URL 인코딩(NFC 폴더 + NFD 파일) 으로 변환
"""
from __future__ import annotations

import re
import sys
import unicodedata
import urllib.parse
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "data" / "weeks.yml"
HEADER_FILE = ROOT / "templates" / "readme_header.md"
OUT_FILE = ROOT / "README.md"

REPO_BASE = "https://github.com/woowacourse-study/2025-troubleshooting/blob/main/"
RAW_BASE = "https://github.com/woowacourse-study/2025-troubleshooting/raw/main/"


def encode_repo_path(rel_path: str, for_raw: bool = False) -> str:
    """Encode a repo-relative path into a GitHub URL (folder NFC, filename NFD)."""
    if not rel_path:
        return ""
    # External URLs passed through
    if rel_path.startswith("http"):
        return rel_path
    parts = rel_path.split("/")
    encoded_parts = []
    for idx, p in enumerate(parts):
        is_file = idx == len(parts) - 1
        norm = unicodedata.normalize("NFD" if is_file else "NFC", p)
        encoded_parts.append(urllib.parse.quote(norm, safe="()"))
    base = RAW_BASE if for_raw else REPO_BASE
    return base + "/".join(encoded_parts)


def thumb_url(rel_path: str | None) -> str:
    if not rel_path:
        return ""
    if rel_path.startswith("http"):
        return rel_path
    return encode_repo_path(rel_path, for_raw=True)


def anchor_for_toc(week: int) -> str:
    return f"#week-{week}"


def format_date(date_str: str) -> tuple[str, str]:
    y, m, d = date_str.split("-")
    long = f"{int(y)}년 {int(m)}월 {int(d)}일"
    short = f"{y}.{int(m)}.{d.zfill(2)}"
    return long, short


def render_toc(weeks: list[dict]) -> str:
    lines = [
        "## 📣 목차",
        "",
        "| 주차 | 발표 주제 및 발표자 |",
        "| :--- | :--- |",
    ]
    for w in weeks:
        long, short = format_date(w["date"])
        items = "<br>".join(
            f"• {p['title']} (👤 {p['presenter']})" for p in w["presentations"]
        )
        lines.append(f"| [**{w['week']}주차** ({short})]({anchor_for_toc(w['week'])}) | {items} |")
    lines.extend(["", "", "<br>", "<br>", ""])
    return "\n".join(lines)


def render_week_section(w: dict) -> str:
    long_date, _ = format_date(w["date"])
    ps = w["presentations"]
    n = len(ps)

    # Title table
    title_cells = " | ".join(p["title"] for p in ps)
    divider = " | ".join([":-:"] * n)
    presenter_cells = " | ".join(p["presenter"] for p in ps)

    out = [
        f'<a id="week-{w["week"]}"></a>',
        "",
        f'## **{w["week"]}주차** ( {long_date} )',
        "",
        f"> | {title_cells} |",
        f"> | {divider} |",
        f"> | {presenter_cells} |",
        "",
        "### 💎 발표자료",
        "",
        "<table>",
    ]

    # Render a 2-column grid of (image, links)
    rows = []
    i = 0
    while i < n:
        left, right = ps[i], ps[i + 1] if i + 1 < n else None
        rows.append((left, right))
        i += 2

    for left, right in rows:
        # image row
        out.append("  <tr>")
        out.append(f'    <td width="50%" align="center">')
        img = thumb_url(left.get("thumbnail"))
        if img:
            out.append(f'      <img src="{img}" width="100%">')
        out.append("    </td>")
        if right:
            out.append(f'    <td width="50%" align="center">')
            img_r = thumb_url(right.get("thumbnail"))
            if img_r:
                out.append(f'      <img src="{img_r}" width="100%">')
            out.append("    </td>")
        else:
            out.append("    <td>&nbsp;</td>")
        out.append("  </tr>")

        # link row
        out.append("  <tr>")
        for cell in (left, right):
            if cell is None:
                out.append("    <td>&nbsp;</td>")
                continue
            pdf_url = encode_repo_path(cell.get("pdf")) if cell.get("pdf") else ""
            yt_url = cell.get("youtube") or ""
            out.append('    <td align="center">')
            out.append(f'      <a href="{pdf_url}">[📚 {cell["title"]}]</a><br>')
            if yt_url:
                out.append(
                    f'      <a href="{yt_url}">[🎥 {w["week"]}주차 발표 영상 - {cell["presenter"]}]</a>'
                )
            out.append("    </td>")
        out.append("  </tr>")

    out.extend(["</table>", "", "---", ""])
    return "\n".join(out)


def main() -> int:
    data = yaml.safe_load(DATA_FILE.read_text())
    weeks = sorted(data["weeks"], key=lambda w: w["week"])

    header = HEADER_FILE.read_text().rstrip() + "\n\n"
    toc = render_toc(weeks)
    sections = "\n".join("<br/>\n" + render_week_section(w) for w in weeks)

    content = header + toc + sections
    OUT_FILE.write_text(content)
    print(f"wrote {OUT_FILE} ({len(weeks)} weeks)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
