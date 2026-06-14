#!/usr/bin/env python3
"""
이슈 폼으로 제출된 유튜브 영상 링크 추가 요청을 처리한다.

입력
  - 환경변수 ISSUE_BODY: 이슈 본문 (Issue Form 형식)

동작
  1) 본문에서 주차/발표자/유튜브 URL 파싱
  2) .automation/weeks.yml에서 (week, presenter) 일치 항목 검색
     - 0개 또는 2개 이상이면 실패하고 이슈에 코멘트로 안내
  3) 해당 항목의 youtube 필드만 갱신 (PDF·썸네일은 건드리지 않음)
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parent.parent.parent
DATA_FILE = ROOT / ".automation" / "weeks.yml"

YOUTUBE_URL_RE = re.compile(
    r"^https?://(?:www\.)?(?:youtube\.com/watch\?|youtu\.be/|youtube\.com/live/)",
    re.IGNORECASE,
)


def parse_issue_body(body: str) -> dict[str, str]:
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


def main() -> int:
    body = os.environ.get("ISSUE_BODY", "")
    if not body.strip():
        fail("이슈 본문이 비어있습니다")

    sections = parse_issue_body(body)
    week_str = sections.get("주차", "").strip()
    presenter = sections.get("발표자", "").strip()
    youtube = sections.get("유튜브 URL", "").strip()

    if not week_str.isdigit():
        fail(f"주차는 숫자여야 합니다: {week_str!r}")
    week = int(week_str)
    if not presenter:
        fail("발표자가 비어있습니다")
    if not youtube:
        fail("유튜브 URL이 비어있습니다")
    if not YOUTUBE_URL_RE.match(youtube):
        fail(f"유튜브 URL 형식이 아닙니다: {youtube!r}")

    with DATA_FILE.open() as f:
        data = yaml.safe_load(f)

    target_week = next((w for w in data["weeks"] if w["week"] == week), None)
    if target_week is None:
        fail(f"W{week}가 weeks.yml에 존재하지 않습니다")

    presentations = target_week.get("presentations", [])
    matches = [p for p in presentations if p.get("presenter") == presenter]

    if len(matches) == 0:
        existing = "\n".join(
            f"  - {p.get('presenter')} / {p.get('title')!r}" for p in presentations
        ) or "  (없음)"
        fail(
            f"W{week}에서 발표자 {presenter!r}의 항목을 찾을 수 없습니다.\n"
            f"현재 등록된 항목:\n{existing}"
        )
    if len(matches) > 1:
        titles = "\n".join(f"  - {p.get('title')!r}" for p in matches)
        fail(
            f"W{week}에 발표자 {presenter!r}의 발표가 {len(matches)}개 있어 하나로 특정할 수 없습니다.\n"
            f"해당 발표 목록:\n{titles}"
        )

    target = matches[0]
    title = target.get("title")
    previous = target.get("youtube") or ""
    if previous == youtube:
        fail(f"이미 같은 유튜브 URL이 등록되어 있습니다: {youtube}")

    target["youtube"] = youtube
    if previous:
        print(f"W{week} ({presenter}, {title!r}) 유튜브 URL 변경: {previous} -> {youtube}")
    else:
        print(f"W{week} ({presenter}, {title!r}) 유튜브 URL 추가: {youtube}")

    with DATA_FILE.open("w") as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False, width=1000)

    set_output("week", str(week))
    set_output("presenter", presenter)
    set_output("title", title)
    set_output("youtube", youtube)
    set_output("previous", previous)
    print("done")
    return 0


if __name__ == "__main__":
    sys.exit(main())
