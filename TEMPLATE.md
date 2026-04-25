# 📝 새 회차 발표자료 등록 가이드

`README.md`는 수동 편집하지 않습니다. 루트의 `weeks.yml`에 데이터만 추가하면 GitHub Actions가 썸네일 추출과 README 재생성을 자동으로 처리합니다.

## 🚀 한 줄 요약

1. PDF를 `NN_N주차/` 폴더에 올리고
2. 루트의 `weeks.yml`에 블록 한 개 추가한 뒤
3. main에 푸시하면 끝.

Action이 돌면서 `.automation/thumbnails/` 아래 첫 페이지 PNG가 생성되고 `README.md`가 자동 커밋됩니다.

---

## ✍️ 데이터 추가 예시

새 회차(예: 17주차)가 추가되는 상황:

```yaml
- week: 17
  date: 2026-04-04
  presentations:
    - title: Redis Pub/Sub 파고들기
      presenter: 돔푸
      pdf: 17_17주차/[발표자료]Redis_Pub_Sub_파고들기(돔푸).pdf
      thumbnail:            # 비워두면 PDF 첫 페이지가 자동 추출됨
      youtube:              # 아직 없으면 비워둠
    - title: 장애 회고 템플릿 만들기
      presenter: 메이
      pdf: 17_17주차/[발표자료]장애_회고_템플릿(메이).pdf
      thumbnail:
      youtube: https://www.youtube.com/watch?v=xxxx
```

## 🔑 필드 설명

| 필드 | 필수 | 설명 |
| :--- | :-: | :--- |
| `week` | ✅ | 주차 번호 (정수) |
| `date` | ✅ | 발표 날짜. `YYYY-MM-DD` 형식 |
| `presentations[].title` | ✅ | 발표 제목 |
| `presentations[].presenter` | ✅ | 발표자 닉네임 |
| `presentations[].pdf` | ✅ | 저장소 내 PDF 경로. 한글 파일명 그대로 사용 가능 |
| `presentations[].thumbnail` | ❌ | 비워두면 PDF 1페이지가 자동 추출되어 `.automation/thumbnails/w{NN}_{발표자}.png`로 저장됨. 외부 이미지 URL을 직접 넣어도 됨 |
| `presentations[].youtube` | ❌ | 발표 영상 URL. 없으면 비워둠 |

## 🖼️ 썸네일 자동 추출

- `pdf` 파일이 있고 `thumbnail`이 비어 있으면 GitHub Actions가 `pdftoppm`으로 첫 페이지를 PNG로 뽑아 `.automation/thumbnails/w{주차2자리}_{발표자}.png`에 저장합니다.
- 추출 후 `weeks.yml`의 `thumbnail` 필드가 자동 채워져 커밋됩니다.
- Keynote를 쓰는 경우 PDF로 export해서 올려주세요. `.pdf`만 지원합니다.
- 자동 추출 결과가 마음에 들지 않으면 `.automation/thumbnails/` 경로의 PNG를 덮어쓰거나, `thumbnail:` 필드에 원하는 이미지 URL을 직접 넣으면 됩니다.

## 🛠️ 로컬에서 직접 돌려보고 싶다면

```bash
# poppler 설치 (macOS)
brew install poppler

pip install pyyaml
python .automation/scripts/generate_thumbnails.py   # 썸네일 추출
python .automation/scripts/generate_readme.py       # README 재생성
```

## ⚠️ 주의

- `README.md`는 자동 생성물입니다. 직접 편집하지 말고 루트의 `weeks.yml`이나 `.automation/templates/readme_header.md`를 수정해야 합니다.
- 스터디 소개, 스터디원, 문의 등 고정 영역은 `.automation/templates/readme_header.md`에 들어 있습니다.
- `.automation/` 디렉터리 하위는 전부 자동화 자산입니다. 발표자는 건드릴 필요 없습니다.
