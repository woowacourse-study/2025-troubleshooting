#!/usr/bin/env python3
"""
이슈 폼으로 제출된 "유튜브 자동 매칭" 요청을 처리한다.

입력
  - 환경변수 ISSUE_BODY: 이슈 본문 (Issue Form 형식, 주차 번호 1개)
  - 환경변수 YOUTUBE_API_KEY: YouTube Data API v3 키
  - (선택) 환경변수 CHANNEL_HANDLE: 채널 핸들 (기본 we-55)

동작
  1) 본문에서 주차 파싱
  2) weeks.yml에서 해당 주차의 youtube 비어있는 발표 수집
  3) 채널 업로드 영상 전체를 가져와 (발표자 일치 + 제목 공백무시 완전일치) 매칭
  4) 자동 매칭된 항목의 youtube를 채우고 weeks.yml 저장
  5) 결과(자동 반영 / 확인 필요 후보)를 코멘트 본문으로 출력
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

import requests
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from youtube_match import find_matches, build_register_url


ROOT = Path(__file__).resolve().parent.parent.parent
DATA_FILE = ROOT / ".automation" / "weeks.yml"
CHANNEL_HANDLE = os.environ.get("CHANNEL_HANDLE", "we-55").lstrip("@")
API_BASE = "https://www.googleapis.com/youtube/v3"


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


def fetch_channel_videos(api_key: str, handle: str) -> list[dict]:
    """채널 업로드 재생목록의 모든 영상을 [{title, video_id}, ...]로 반환."""
    r = requests.get(
        f"{API_BASE}/channels",
        params={"part": "contentDetails", "forHandle": handle, "key": api_key},
        timeout=30,
    )
    if r.status_code != 200:
        fail(f"채널 조회 실패: HTTP {r.status_code} {r.text[:200]}")
    items = r.json().get("items", [])
    if not items:
        fail(f"채널을 찾을 수 없습니다: @{handle}")
    uploads = items[0]["contentDetails"]["relatedPlaylists"]["uploads"]

    videos: list[dict] = []
    page_token = None
    while True:
        params = {
            "part": "snippet",
            "playlistId": uploads,
            "maxResults": 50,
            "key": api_key,
        }
        if page_token:
            params["pageToken"] = page_token
        r = requests.get(f"{API_BASE}/playlistItems", params=params, timeout=30)
        if r.status_code != 200:
            fail(f"영상 목록 조회 실패: HTTP {r.status_code} {r.text[:200]}")
        data = r.json()
        for it in data.get("items", []):
            sn = it["snippet"]
            vid = sn.get("resourceId", {}).get("videoId")
            if vid:
                videos.append({"title": sn.get("title", ""), "video_id": vid})
        page_token = data.get("nextPageToken")
        if not page_token:
            break
    return videos


def build_comment(week: int, result: dict, repo: str) -> str:
    auto = result["auto"]
    candidates = result["candidates"]
    lines = [f"## 🎬 {week}주차 유튜브 자동 매칭 결과", ""]

    lines.append(f"### ✅ 자동 반영 ({len(auto)}건)")
    if auto:
        for pres, url in auto:
            lines.append(f"- **{pres['presenter']}** / {pres['title']} → {url}")
    else:
        lines.append("- (없음)")
    lines.append("")

    lines.append(f"### ❓ 확인 필요 ({len(candidates)}건)")
    if candidates:
        lines.append("아래 항목은 제목이 정확히 일치하지 않아 자동 반영하지 않았습니다. 후보가 맞다면 **[✅ 이걸로 등록]** 링크를 눌러주세요 (폼이 미리 채워진 채 열리고, Submit하면 등록됩니다).")
        for pres, cands in candidates:
            lines.append(f"- **{pres['presenter']}** / {pres['title']}")
            if cands:
                for v in cands:
                    watch = f"https://www.youtube.com/watch?v={v['video_id']}"
                    reg = build_register_url(repo, week, pres["presenter"], watch)
                    lines.append(f"  - 후보: [{v['title']}]({watch}) → [✅ 이걸로 등록]({reg})")
            else:
                lines.append("  - 후보: (발표자가 일치하는 영상 없음)")
    else:
        lines.append("- (없음)")

    return "\n".join(lines)


def main() -> int:
    body = os.environ.get("ISSUE_BODY", "")
    if not body.strip():
        fail("이슈 본문이 비어있습니다")

    api_key = os.environ.get("YOUTUBE_API_KEY", "").strip()
    if not api_key:
        fail("YOUTUBE_API_KEY 시크릿이 설정되어 있지 않습니다")

    sections = parse_issue_body(body)
    week_str = sections.get("주차", "").strip()
    if not week_str.isdigit():
        fail(f"주차는 숫자여야 합니다: {week_str!r}")
    week = int(week_str)

    with DATA_FILE.open() as f:
        data = yaml.safe_load(f)

    target_week = next((w for w in data["weeks"] if w["week"] == week), None)
    if target_week is None:
        fail(f"W{week}가 weeks.yml에 존재하지 않습니다")

    presentations = target_week.get("presentations", [])
    empty = [p for p in presentations if not p.get("youtube")]
    if not empty:
        set_output("auto_count", "0")
        set_output("pending_count", "0")
        set_output("comment", f"## 🎬 {week}주차 유튜브 자동 매칭 결과\n\n비어있는 유튜브 링크가 없습니다. 모든 발표에 이미 링크가 등록되어 있습니다.")
        print(f"W{week}: 비어있는 항목 없음")
        return 0

    print(f"채널 영상 조회: @{CHANNEL_HANDLE}")
    videos = fetch_channel_videos(api_key, CHANNEL_HANDLE)
    print(f"영상 {len(videos)}개 조회됨")

    result = find_matches(presentations, videos)

    # 자동 매칭된 항목의 youtube 필드를 실제로 채운다 (presentations 내 dict 직접 갱신)
    for pres, url in result["auto"]:
        pres["youtube"] = url
        print(f"자동 반영: W{week} {pres['presenter']} {pres['title']!r} -> {url}")

    if result["auto"]:
        with DATA_FILE.open("w") as f:
            yaml.dump(data, f, allow_unicode=True, sort_keys=False, width=1000)

    repo = os.environ.get("GITHUB_REPOSITORY", "woowacourse-study/2025-troubleshooting")
    set_output("auto_count", str(len(result["auto"])))
    set_output("pending_count", str(len(result["candidates"])))
    set_output("week", str(week))
    set_output("comment", build_comment(week, result, repo))
    print("done")
    return 0


if __name__ == "__main__":
    sys.exit(main())
