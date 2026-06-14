# 유튜브 링크 자동 매칭 — 설계

## 배경 / 목적

발표자료(`weeks.yml`)에는 발표마다 `youtube` 링크 필드가 있지만, 영상이 나중에 올라오는 경우가 많아 비어 있는(`null`) 항목이 다수다. 지금은 사람이 [유튜브] 이슈에 주차·발표자·URL을 직접 입력해야 한다.

이 기능은 **주차 번호만 입력하면**, 해당 주차에서 링크가 비어 있는 발표들을 우리 유튜브 채널(`@we-55`)의 이미 올라온 영상과 자동으로 매칭해 채워준다. 영상 제목과 발표자료 제목이 미묘하게 다른 경우가 있어, **오매칭을 0에 가깝게** 하는 보수적 매칭이 핵심 요구사항이다.

## 사용 흐름

1. **"[유튜브 자동매칭]" 이슈 템플릿에 주차 번호만 입력** (예: `20`), 라벨 `youtube-auto` 자동 부여
2. 워크플로가 그 주차의 `youtube == null`인 발표들을 수집
3. `@we-55` 채널의 업로드 영상 전체와 매칭
4. **고신뢰(아래 규칙)는 자동으로 채움**, 나머지는 후보를 이슈 코멘트로 제시
5. 자동 반영분이 있으면 `weeks.yml` 저장 → README 재생성 → 커밋·푸시
6. 이슈에 결과 요약(`자동 반영 N건 / 확인 필요 M건` + 후보 링크) 코멘트 후 close

## 매칭 규칙 (보수적, 오매칭 방지 최우선)

- **정규화**: 문자열에서 모든 공백 문자를 제거 (`re.sub(r"\s+", "", s)`). 그 외 글자는 보존.
- **발표자**: 정규화 후 영상 발표자 == weeks.yml 발표자여야 함
- **제목**: 정규화 후 **완전 일치(100%)**여야 자동 반영
  - `"메시지 저장 구조 설계"` ↔ `"메시지저장구조설계"` → ✅
  - `"신비로운 인덱스지식"` ↔ `"신비한 인덱스 지식"` → ❌ (자동 반영 안 함 → 후보로만 제시)
- 자동 반영 조건을 못 채운 빈 항목은 → **발표자가 일치하는 영상들**을 후보로 코멘트에 제시(없으면 "후보 없음")

## YouTube Data API 사용 (quota 절약)

1. 핸들 → 채널 ID: `channels?part=contentDetails&forHandle=we-55`
   - 응답에서 `contentDetails.relatedPlaylists.uploads` (업로드 재생목록 ID) 획득
2. 업로드 재생목록 → 영상 목록: `playlistItems?part=snippet&playlistId=<uploads>&maxResults=50` 페이지네이션
   - 각 영상: `snippet.title`, `snippet.resourceId.videoId`
3. 링크: `https://www.youtube.com/watch?v=<videoId>`
4. 영상 제목 파싱: 마지막 `|` 기준으로 `{제목} | {발표자}` 분리. `|`가 없으면 발표자 미상으로 처리(제목 전체만 비교 대상에서 제외 → 후보군에서도 제외)

> `search` API(100 units) 대신 `playlistItems`(1 unit/페이지)를 사용해 quota를 아낀다. 채널 영상 ~100개면 2~3회 호출.

## 신규 파일 (기존 파일·로직 무수정)

| 파일 | 역할 |
|---|---|
| `.github/ISSUE_TEMPLATE/youtube-auto.yml` | 라벨 `youtube-auto`, 입력: 주차 1개 |
| `.github/workflows/process-youtube-auto.yml` | `secrets.YOUTUBE_API_KEY` 사용, 기존 워크플로와 동일 골격 |
| `.automation/scripts/process_youtube_auto_issue.py` | 주차 파싱 → API 조회 → 매칭 → weeks.yml 갱신 |

- 라벨 `youtube-auto`는 레포에 미리 생성해야 이슈에 자동으로 붙는다(이전에 `youtube` 라벨 누락으로 skip됐던 교훈 반영).
- 워크플로 `concurrency: group: main-writer` 공유로 기존 자동화와 push 충돌 방지.

## 안전장치

- 이미 `youtube`가 채워진 항목은 **절대 덮어쓰지 않음**
- API 키 없음/호출 실패/주차 없음 → `::error::` + 이슈 코멘트로 안내하고 실패 종료
- 자동 반영 0건이면 커밋 없이, 후보 안내 코멘트만 남기고 close

## 검증 방법

- 로컬: `weeks.yml` 임시 복사본 + 가짜 영상 목록(JSON)으로 매칭 함수 단위 테스트 (공백 무시 일치 / 단어 불일치 → 후보 / 발표자 불일치 → 제외 / 이미 채워진 항목 스킵)
- API 연동: 실제 키로 `@we-55` 채널 영상 조회가 되는지 1회 확인(읽기 전용)
- 실제: 20주차 이슈로 end-to-end 동작 확인(자동 반영 + 후보 코멘트)
