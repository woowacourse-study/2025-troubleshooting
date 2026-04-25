#!/usr/bin/env python3
"""
이슈 폼으로 제출된 발표자료 업로드 요청을 처리한다.

입력
  - 환경변수 ISSUE_BODY: 이슈 본문 (Issue Form 형식)
  - 환경변수 GITHUB_TOKEN: user-attachments 다운로드용

동작
  1) 본문에서 주차/발표 일자/발표자/제목/유튜브/PDF 링크 파싱
  2) PDF 다운로드 (NFC 정규화된 파일명으로 저장)
  3) weeks.yml에 항목 추가 (해당 주차가 없으면 새 주차 생성)
"""
from __future__ import annotations

import os
import re
import sys
import unicodedata
from pathlib import Path

import requests
import yaml


ROOT = Path(__file__).resolve().parent.parent.parent
DATA_FILE = ROOT / "weeks.yml"

NO_RESPONSE_PLACEHOLDERS = {"", "_No response_"}


def parse_issue_body(body: str) -> dict[str, str]:
    """`### 헤딩` 블록을 키-값 dict로."""
    sections: dict[str, str] = {}
    current_key: str | None = None
    current_lines: list[str] = []
    for line in body.replace("\r\n", "\n").split("\n"):
        m = re.match(r"^###\s+(.+?)\s*$", line)
        if m:
            if current_key is not None:
                sections[current_key] = "\n".join(current_lines).strip()
            current_key = m.group(1).strip()
            current_lines = []
        else:
            current_lines.append(line)
    if current_key is not None:
        sections[current_key] = "\n".join(current_lines).strip()
    return sections


def extract_pdf_url(text: str) -> str | None:
    m = re.search(r"\[([^\]]+\.pdf)\]\((https?://[^\)]+)\)", text, re.IGNORECASE)
    return m.group(2) if m else None


def slugify_filename(title: str) -> str:
    cleaned = re.sub(r'[\\/:*?"<>|]', "_", title).strip()
    cleaned = unicodedata.normalize("NFC", cleaned)
    return cleaned or "untitled"


def set_output(name: str, value: str) -> None:
    out = os.environ.get("GITHUB_OUTPUT")
    if not out:
        return
    with open(out, "a") as f:
        f.write(f"{name}<<__EOF__\n{value}\n__EOF__\n")


def fail(msg: str) -> None:
    set_output("error", msg)
    print(f"::error::{msg}", file=sys.stderr)
    sys.exit(1)


def download_pdf(url: str) -> bytes:
    headers = {"Accept": "application/octet-stream"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    resp = requests.get(url, headers=headers, timeout=120, allow_redirects=True)
    if resp.status_code != 200:
        fail(f"PDF 다운로드 실패: HTTP {resp.status_code}")
    if not resp.content.startswith(b"%PDF"):
        fail("받은 파일이 PDF가 아닙니다")
    return resp.content


def main() -> int:
    body = os.environ.get("ISSUE_BODY", "")
    if not body.strip():
        fail("이슈 본문이 비어있습니다")

    sections = parse_issue_body(body)

    week_str = sections.get("주차", "").strip()
    date = sections.get("발표 일자", "").strip()
    presenter = sections.get("발표자", "").strip()
    title = sections.get("제목", "").strip()
    youtube_raw = sections.get("유튜브 URL", "").strip()
    pdf_field = sections.get("PDF 파일", "")

    if not week_str.isdigit():
        fail(f"주차는 숫자여야 합니다: {week_str!r}")
    week = int(week_str)
    if week < 1 or week > 999:
        fail(f"주차 범위 초과: {week}")
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", date):
        fail(f"발표 일자 형식이 잘못되었습니다 (YYYY-MM-DD 필요): {date!r}")
    if not presenter:
        fail("발표자가 비어있습니다")
    if not title:
        fail("제목이 비어있습니다")

    youtube = None if youtube_raw in NO_RESPONSE_PLACEHOLDERS else youtube_raw

    pdf_url = extract_pdf_url(pdf_field)
    if not pdf_url:
        fail("PDF 첨부 링크를 본문에서 찾을 수 없습니다")

    print(f"PDF 다운로드: {pdf_url}")
    pdf_bytes = download_pdf(pdf_url)

    week_dir_name = f"{week:02d}_{week}주차"
    week_dir = ROOT / week_dir_name
    week_dir.mkdir(parents=True, exist_ok=True)

    file_basename = slugify_filename(title) + ".pdf"
    pdf_path = week_dir / file_basename
    if pdf_path.exists():
        fail(f"이미 같은 경로에 파일이 있습니다: {pdf_path.relative_to(ROOT)}")
    pdf_path.write_bytes(pdf_bytes)
    print(f"저장: {pdf_path.relative_to(ROOT)} ({len(pdf_bytes):,} bytes)")

    pdf_rel = f"{week_dir_name}/{file_basename}"

    with DATA_FILE.open() as f:
        data = yaml.safe_load(f)

    target_week = next((w for w in data["weeks"] if w["week"] == week), None)

    new_entry = {
        "title": title,
        "presenter": presenter,
        "pdf": pdf_rel,
        "thumbnail": None,
        "youtube": youtube,
    }

    if target_week is None:
        data["weeks"].append({
            "week": week,
            "date": date,
            "presentations": [new_entry],
        })
        data["weeks"].sort(key=lambda w: w["week"])
        print(f"새 주차 생성: W{week} ({date})")
    else:
        for p in target_week.get("presentations", []):
            if p.get("presenter") == presenter and p.get("title") == title:
                fail(f"이미 같은 항목이 등록되어 있습니다: W{week} {presenter} {title!r}")
        target_week.setdefault("presentations", []).append(new_entry)
        print(f"기존 주차에 추가: W{week}")

    with DATA_FILE.open("w") as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False, width=1000)

    set_output("week", str(week))
    set_output("presenter", presenter)
    set_output("title", title)
    set_output("pdf_path", pdf_rel)
    print("done")
    return 0


if __name__ == "__main__":
    sys.exit(main())
