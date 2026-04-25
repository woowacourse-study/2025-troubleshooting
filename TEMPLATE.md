# 📝 주차별 섹션 작성 템플릿

이 파일은 `README.md`에 새로운 주차를 추가할 때 복사해서 사용하는 템플릿입니다.

## 🧭 사용 방법

1. **목차 테이블에 한 줄 추가** — `README.md` 상단의 `## 📣 목차` 표에 새 주차 행을 추가합니다.
2. **해당 주차의 발표자 수에 맞는 섹션 템플릿**(아래 1~4인용 블록 중 하나)을 복사해서 `README.md` 맨 아래에 붙여넣습니다.
3. 아래 **치환 키 표**를 참고해 `{{ ... }}` 플레이스홀더를 실제 값으로 교체합니다.
4. 발표자료 PDF를 `NN_N주차/` 폴더에 올리고, 발표자료 링크는 GitHub raw/blob 경로로 연결합니다.
5. 썸네일 이미지는 GitHub Issues/PR 또는 업로드를 통해 얻은 `user-attachments` URL을 사용합니다.
6. 아직 영상이 없는 경우 `[🎥 ...]` 줄을 `<!-- ... -->` 주석으로 감싸두고, 추후 업로드 시 해제합니다.

---

## 🔑 치환 키 표

| 플레이스홀더 | 설명 | 예시 |
| :--- | :--- | :--- |
| `{{WEEK_NUM}}` | 주차 번호 (숫자) | `17` |
| `{{WEEK_NUM_2D}}` | 주차 번호 (2자리, 디렉터리용) | `17` |
| `{{YEAR}}` | 발표 연도 | `2026` |
| `{{MONTH}}` | 발표 월 (앞자리 0 없이) | `4` |
| `{{DAY}}` | 발표 일 (앞자리 0 없이) | `11` |
| `{{DIR_PATH}}` | URL-encoded 폴더 경로 (`NN_N%EC%A3%BC%EC%B0%A8`) | `17_17%EC%A3%BC%EC%B0%A8` |
| `{{TITLE_N}}` | N번째 발표 제목 | `Redis Pub/Sub 파고들기` |
| `{{PRESENTER_N}}` | N번째 발표자 닉네임 | `돔푸` |
| `{{IMG_URL_N}}` | N번째 썸네일 이미지 URL | `https://github.com/user-attachments/assets/xxxx` |
| `{{PDF_URL_N}}` | N번째 발표자료 PDF 링크 | `https://github.com/woowacourse-study/2025-troubleshooting/blob/main/17_17%EC%A3%BC%EC%B0%A8/xxx.pdf` |
| `{{YOUTUBE_URL_N}}` | N번째 발표 영상 URL | `https://www.youtube.com/watch?v=xxxx` |

> 💡 **목차 앵커**: 주차 섹션에는 `<a id="week-{{WEEK_NUM}}"></a>`를 반드시 붙여 목차 링크(`#{{WEEK_NUM}}주차--{{YEAR}}년-{{MONTH}}월-{{DAY}}일-`)와 호환되게 합니다.

---

## 📑 목차 행 템플릿 (1줄)

```markdown
| [**{{WEEK_NUM}}주차** ({{YEAR}}.{{MONTH_2D}}.{{DAY_2D}})](#week-{{WEEK_NUM}}) | • {{TITLE_1}} (👤 {{PRESENTER_1}})<br>• {{TITLE_2}} (👤 {{PRESENTER_2}})<br>• {{TITLE_3}} (👤 {{PRESENTER_3}}) |
```

> 발표자 수에 맞게 `<br>•` 라인을 추가/삭제합니다.

---

## 🎤 1인 발표용 템플릿

```markdown
<br/>
<a id="week-{{WEEK_NUM}}"></a>

## **{{WEEK_NUM}}주차** ( {{YEAR}}년 {{MONTH}}월 {{DAY}}일 )

> | {{TITLE_1}} |
> | :-: |
> | {{PRESENTER_1}} |

### 💎 발표자료

<table>
  <tr>
    <td width="50%" align="center">
      <img src="{{IMG_URL_1}}" width="100%">
    </td>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <td align="center">
      <a href="{{PDF_URL_1}}">[📚 {{TITLE_1}}]</a><br>
      <a href="{{YOUTUBE_URL_1}}">[🎥 {{WEEK_NUM}}주차 발표 영상 - {{PRESENTER_1}}]</a>
    </td>
    <td>&nbsp;</td>
  </tr>
</table>

---
```

---

## 🎤🎤 2인 발표용 템플릿

```markdown
<br/>
<a id="week-{{WEEK_NUM}}"></a>

## **{{WEEK_NUM}}주차** ( {{YEAR}}년 {{MONTH}}월 {{DAY}}일 )

> | {{TITLE_1}} | {{TITLE_2}} |
> | :-: | :-: |
> | {{PRESENTER_1}} | {{PRESENTER_2}} |

### 💎 발표자료

<table>
  <tr>
    <td width="50%" align="center">
      <img src="{{IMG_URL_1}}" width="100%">
    </td>
    <td width="50%" align="center">
      <img src="{{IMG_URL_2}}" width="100%">
    </td>
  </tr>
  <tr>
    <td align="center">
      <a href="{{PDF_URL_1}}">[📚 {{TITLE_1}}]</a><br>
      <a href="{{YOUTUBE_URL_1}}">[🎥 {{WEEK_NUM}}주차 발표 영상 - {{PRESENTER_1}}]</a>
    </td>
    <td align="center">
      <a href="{{PDF_URL_2}}">[📚 {{TITLE_2}}]</a><br>
      <a href="{{YOUTUBE_URL_2}}">[🎥 {{WEEK_NUM}}주차 발표 영상 - {{PRESENTER_2}}]</a>
    </td>
  </tr>
</table>

---
```

---

## 🎤🎤🎤 3인 발표용 템플릿

```markdown
<br/>
<a id="week-{{WEEK_NUM}}"></a>

## **{{WEEK_NUM}}주차** ( {{YEAR}}년 {{MONTH}}월 {{DAY}}일 )

> | {{TITLE_1}} | {{TITLE_2}} | {{TITLE_3}} |
> | :-: | :-: | :-: |
> | {{PRESENTER_1}} | {{PRESENTER_2}} | {{PRESENTER_3}} |

### 💎 발표자료

<table>
  <tr>
    <td width="50%" align="center">
      <img src="{{IMG_URL_1}}" width="100%">
    </td>
    <td width="50%" align="center">
      <img src="{{IMG_URL_2}}" width="100%">
    </td>
  </tr>
  <tr>
    <td align="center">
      <a href="{{PDF_URL_1}}">[📚 {{TITLE_1}}]</a><br>
      <a href="{{YOUTUBE_URL_1}}">[🎥 {{WEEK_NUM}}주차 발표 영상 - {{PRESENTER_1}}]</a>
    </td>
    <td align="center">
      <a href="{{PDF_URL_2}}">[📚 {{TITLE_2}}]</a><br>
      <a href="{{YOUTUBE_URL_2}}">[🎥 {{WEEK_NUM}}주차 발표 영상 - {{PRESENTER_2}}]</a>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center">
      <img src="{{IMG_URL_3}}" width="100%">
    </td>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <td align="center">
      <a href="{{PDF_URL_3}}">[📚 {{TITLE_3}}]</a><br>
      <a href="{{YOUTUBE_URL_3}}">[🎥 {{WEEK_NUM}}주차 발표 영상 - {{PRESENTER_3}}]</a>
    </td>
    <td>&nbsp;</td>
  </tr>
</table>

---
```

---

## 🎤🎤🎤🎤 4인 발표용 템플릿

```markdown
<br/>
<a id="week-{{WEEK_NUM}}"></a>

## **{{WEEK_NUM}}주차** ( {{YEAR}}년 {{MONTH}}월 {{DAY}}일 )

> | {{TITLE_1}} | {{TITLE_2}} | {{TITLE_3}} | {{TITLE_4}} |
> | :-: | :-: | :-: | :-: |
> | {{PRESENTER_1}} | {{PRESENTER_2}} | {{PRESENTER_3}} | {{PRESENTER_4}} |

### 💎 발표자료

<table>
  <tr>
    <td width="50%" align="center">
      <img src="{{IMG_URL_1}}" width="100%">
    </td>
    <td width="50%" align="center">
      <img src="{{IMG_URL_2}}" width="100%">
    </td>
  </tr>
  <tr>
    <td align="center">
      <a href="{{PDF_URL_1}}">[📚 {{TITLE_1}}]</a><br>
      <a href="{{YOUTUBE_URL_1}}">[🎥 {{WEEK_NUM}}주차 발표 영상 - {{PRESENTER_1}}]</a>
    </td>
    <td align="center">
      <a href="{{PDF_URL_2}}">[📚 {{TITLE_2}}]</a><br>
      <a href="{{YOUTUBE_URL_2}}">[🎥 {{WEEK_NUM}}주차 발표 영상 - {{PRESENTER_2}}]</a>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center">
      <img src="{{IMG_URL_3}}" width="100%">
    </td>
    <td width="50%" align="center">
      <img src="{{IMG_URL_4}}" width="100%">
    </td>
  </tr>
  <tr>
    <td align="center">
      <a href="{{PDF_URL_3}}">[📚 {{TITLE_3}}]</a><br>
      <a href="{{YOUTUBE_URL_3}}">[🎥 {{WEEK_NUM}}주차 발표 영상 - {{PRESENTER_3}}]</a>
    </td>
    <td align="center">
      <a href="{{PDF_URL_4}}">[📚 {{TITLE_4}}]</a><br>
      <a href="{{YOUTUBE_URL_4}}">[🎥 {{WEEK_NUM}}주차 발표 영상 - {{PRESENTER_4}}]</a>
    </td>
  </tr>
</table>

---
```

---

## ✅ 체크리스트

- [ ] `NN_N주차/` 폴더 생성 및 PDF 업로드
- [ ] `## 📣 목차` 테이블에 행 추가
- [ ] 해당 주차 섹션 블록 추가 (`<a id="week-N">` 앵커 포함)
- [ ] 모든 `{{ ... }}` 플레이스홀더 치환 완료
- [ ] 발표 영상이 아직 없다면 `<!-- ... -->`로 주석 처리
- [ ] 미리보기에서 표·이미지·링크가 정상 렌더되는지 확인
