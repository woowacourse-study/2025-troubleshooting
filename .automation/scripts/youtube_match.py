"""
유튜브 영상 ↔ 발표자료 매칭 순수 로직 (API/네트워크 의존 없음).

매칭 규칙 (보수적, 오매칭 방지 최우선):
  - 정규화: 모든 공백 제거
  - 발표자: 정규화 후 완전 일치
  - 제목: 정규화 후 완전 일치(100%, 띄어쓰기만 무시)해야 자동 매칭
  - 자동 매칭 안 된 빈 항목 → 발표자가 일치하는 영상을 후보로 제시
"""
from __future__ import annotations

import re
from urllib.parse import quote

WATCH_URL = "https://www.youtube.com/watch?v={}"
MANUAL_TEMPLATE = "youtube-presentation.yml"


def normalize(s: str | None) -> str:
    """모든 공백 문자를 제거한다."""
    if not s:
        return ""
    return re.sub(r"\s+", "", s)


def parse_video_title(video_title: str) -> tuple[str, str] | None:
    """'제목 | 발표자' 형식을 (제목, 발표자)로 분리. '|'가 없으면 None.

    마지막 '|'를 발표자 구분자로 사용한다.
    """
    if "|" not in video_title:
        return None
    title, _, presenter = video_title.rpartition("|")
    return title.strip(), presenter.strip()


def build_register_url(repo: str, week: int, presenter: str, youtube_url: str) -> str:
    """수동추가 이슈 폼을 미리 채운 채로 여는 URL을 만든다.

    클릭하면 '유튜브 링크 수동 추가' 폼이 주차/발표자/유튜브 URL까지 채워진 상태로
    열리고, 사용자가 Submit만 하면 기존 youtube 워크플로가 등록을 처리한다.
    """
    params = "&".join([
        f"template={MANUAL_TEMPLATE}",
        f"week={quote(str(week))}",
        f"presenter={quote(presenter)}",
        f"youtube={quote(youtube_url)}",
    ])
    return f"https://github.com/{repo}/issues/new?{params}"


def find_matches(presentations: list[dict], videos: list[dict]) -> dict:
    """주차의 발표 항목들을 채널 영상과 매칭한다.

    presentations: weeks.yml 한 주차의 발표 리스트 (dict: title, presenter, youtube, ...)
    videos: 채널 영상 리스트 (dict: title='제목 | 발표자', video_id)

    반환 dict:
      auto:           [(presentation, video_url), ...]  자동 반영 대상
      candidates:     [(presentation, [video, ...]), ...]  확인 필요(발표자 일치 영상이 후보)
      skipped_filled: [presentation, ...]  이미 youtube가 있어 건너뛴 항목
    """
    # 영상 제목 파싱: (정규화제목, 정규화발표자, video) 목록
    parsed = []
    for v in videos:
        pt = parse_video_title(v.get("title", ""))
        if pt is None:
            continue
        v_title, v_presenter = pt
        parsed.append((normalize(v_title), normalize(v_presenter), v))

    auto: list[tuple[dict, str]] = []
    candidates: list[tuple[dict, list[dict]]] = []
    skipped_filled: list[dict] = []

    for pres in presentations:
        if pres.get("youtube"):
            skipped_filled.append(pres)
            continue

        n_title = normalize(pres.get("title"))
        n_presenter = normalize(pres.get("presenter"))

        # 발표자가 일치하는 영상들
        presenter_videos = [
            (vt, v) for (vt, vp, v) in parsed if vp == n_presenter
        ]

        exact = [v for (vt, v) in presenter_videos if vt == n_title]
        if exact:
            auto.append((pres, WATCH_URL.format(exact[0]["video_id"])))
        else:
            candidates.append((pres, [v for (_, v) in presenter_videos]))

    return {"auto": auto, "candidates": candidates, "skipped_filled": skipped_filled}
