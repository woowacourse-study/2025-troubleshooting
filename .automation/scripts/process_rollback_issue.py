#!/usr/bin/env python3
"""
이슈 폼으로 제출된 발표자료 롤백(삭제) 요청을 처리한다.

입력
  - 환경변수 ISSUE_BODY: 이슈 본문 (Issue Form 형식)

동작
  1) 본문에서 주차/발표자/제목 파싱
  2) .automation/weeks.yml에서 (week, presenter, title) 일치 항목 검색
     - 0개 또는 2개 이상이면 실패하고 이슈에 코멘트로 안내
  3) PDF / 썸네일 PNG 삭제, weeks.yml에서 항목 제거
  4) 해당 주차의 발표가 0개가 되면 주차 자체를 yml에서 제거하고 빈 디렉터리도 정리
"""
from __future__ import annotations

import os
import re
import sys
import unicodedata
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parent.parent.parent
DATA_FILE = ROOT / ".automation" / "weeks.yml"
THUMB_REL_PREFIX = ".automation/thumbnails/"


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
    title = sections.get("제목", "").strip()

    if not week_str.isdigit():
        fail(f"주차는 숫자여야 합니다: {week_str!r}")
    week = int(week_str)
    if not presenter:
        fail("발표자가 비어있습니다")
    if not title:
        fail("제목이 비어있습니다")

    with DATA_FILE.open() as f:
        data = yaml.safe_load(f)

    target_week = next((w for w in data["weeks"] if w["week"] == week), None)
    if target_week is None:
        fail(f"W{week}가 weeks.yml에 존재하지 않습니다")

    presentations = target_week.get("presentations", [])
    matches = [
        (i, p) for i, p in enumerate(presentations)
        if p.get("presenter") == presenter and p.get("title") == title
    ]

    if len(matches) == 0:
        existing = "\n".join(
            f"  - {p.get('presenter')} / {p.get('title')!r}" for p in presentations
        ) or "  (없음)"
        fail(
            f"W{week}에서 ({presenter}, {title!r}) 항목을 찾을 수 없습니다.\n"
            f"현재 등록된 항목:\n{existing}"
        )
    if len(matches) > 1:
        fail(f"W{week}에 ({presenter}, {title!r}) 항목이 {len(matches)}개 있습니다 (중복)")

    idx, target = matches[0]
    pdf_rel = target.get("pdf") or ""
    thumb_rel = target.get("thumbnail") or ""

    pdf_deleted = ""
    if pdf_rel:
        pdf_path = ROOT / unicodedata.normalize("NFC", pdf_rel)
        if pdf_path.exists():
            pdf_path.unlink()
            print(f"삭제: {pdf_rel}")
            pdf_deleted = pdf_rel
        else:
            print(f"warn: PDF 파일이 이미 없습니다: {pdf_rel}", file=sys.stderr)
            pdf_deleted = pdf_rel

    thumb_deleted = ""
    if thumb_rel and thumb_rel.startswith(THUMB_REL_PREFIX):
        thumb_path = ROOT / unicodedata.normalize("NFC", thumb_rel)
        if thumb_path.exists():
            thumb_path.unlink()
            print(f"삭제: {thumb_rel}")
            thumb_deleted = thumb_rel
        else:
            print(f"warn: 썸네일이 이미 없습니다: {thumb_rel}", file=sys.stderr)
            thumb_deleted = thumb_rel

    presentations.pop(idx)

    week_dir_removed = ""
    if not presentations:
        data["weeks"] = [w for w in data["weeks"] if w["week"] != week]
        week_dir_name = unicodedata.normalize("NFC", f"{week:02d}_{week}주차")
        week_dir = ROOT / week_dir_name
        if week_dir.exists() and week_dir.is_dir():
            try:
                week_dir.rmdir()
                print(f"빈 주차 디렉터리 제거: {week_dir_name}")
                week_dir_removed = week_dir_name
            except OSError:
                print(
                    f"warn: {week_dir_name}에 다른 파일이 남아있어 디렉터리는 유지합니다",
                    file=sys.stderr,
                )
        print(f"W{week} 주차 자체를 weeks.yml에서 제거")
    else:
        print(f"W{week}에서 ({presenter}, {title!r}) 제거")

    with DATA_FILE.open("w") as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False, width=1000)

    set_output("week", str(week))
    set_output("presenter", presenter)
    set_output("title", title)
    set_output("pdf_path", pdf_deleted)
    set_output("thumb_path", thumb_deleted)
    set_output("week_dir_removed", week_dir_removed)
    print("done")
    return 0


if __name__ == "__main__":
    sys.exit(main())
