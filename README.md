# 📚 Troubleshooting

## 🌟 트러블슈팅 스터디 소개 🌟

트러블슈팅 스터디는    
“나만의 문제”를 꺼내서 함께 이야기하고, 해결 과정까지 공유하는 스터디입니다.    

각자 프로젝트에서 겪은 장애, 버그, 성능 이슈, 새로운 기능 도입 시 생긴 시행착오 등을    
직접 발표하고, 스터디원들과 함께 토론하면서    
“왜 이런 문제가 생겼는지, 다음엔 어떻게 더 잘할 수 있을지”를 끝까지 파고듭니다.    

우리는 정답을 아는 사람이 가르치는 스터디가 아니라,   
각자의 경험을 공유하면서 같이 배우며 성장하는 스터디를 지향합니다.   
누군가의 장애 복구 과정이 다른 사람에게는 사전 예방서가 되고,   
한 번의 토론이 팀 설계나 코드 리뷰 방식까지 바뀌는 계기가 되기도 합니다.   

이 스터디의 목표는 단순히 문제 하나를 해결하는 것이 아니라,   
문제를 대하는 사고방식과 함께 성장하는 개발 문화를 함께 만들어 가는 것입니다.    
매주 조금씩, 그러나 꾸준히 서로의 경험을 나누며   
“혼자였다면 절대 못 봤을 관점들”을 함께 쌓아갑니다.   

<br>

## 🚀 스터디원

<table>
  <tr height="140px">
    <td align="center">
      <a href="https://github.com/Ryan-Dia">
        <img src="https://avatars1.githubusercontent.com/u/76567238" alt="새로이" width="100" />
      </a>
      <br />
      <a href="https://github.com/Ryan-Dia">새로이 💻</a>
    </td>
    <td align="center">
      <a href="https://github.com/taek2222">
        <img src="https://avatars.githubusercontent.com/u/118153233?v=4" alt="비타" width="100" />
      </a>
      <br />
      <a href="https://github.com/taek2222">비타 💻</a>
    </td>
    <td align="center">
      <a href="https://github.com/Starlight258">
        <img src="https://avatars.githubusercontent.com/u/78211281?v=4" alt="밍트" width="100" />
      </a>
      <br />
      <a href="https://github.com/Starlight258">밍트 💻</a>
    </td>
    <td align="center">
      <a href="https://github.com/seaniiio">
        <img src="https://avatars.githubusercontent.com/u/121426422?v=4" alt="메이" width="100" />
      </a>
      <br />
      <a href="https://github.com/seaniiio">메이 💻</a>
    </td>
      <td align="center">
      <a href="https://github.com/songsunkook">
        <img src="https://avatars.githubusercontent.com/u/21010656?v=4" alt="모코" width="100" />
      </a>
      <br />
      <a href="https://github.com/songsunkook">모코 💻</a>
    </td>
    </td>
      <td align="center">
      <a href="https://github.com/2Jin1031">
        <img src="https://avatars.githubusercontent.com/u/111180367?v=4" alt="칼리" width="100" />
      </a>
      <br />
      <a href="https://github.com/2Jin1031">칼리 💻</a>
    </td>
    <td align="center">
      <a href="https://github.com/praisebak">
        <img src="https://avatars.githubusercontent.com/u/60121346?v=4" alt="투다" width="100" />
      </a>
      <br />
      <a href="https://github.com/praisebak">투다 💻</a>
    </td>
  </tr>
</table>


<br>
<br>

## 📣 목차

- [1주차 (7월 27일)](#week-1)
  - 21일간의 리딩 실험하기 – 밍트
  - 모니터링 – 투다
  - 테스트 환경의 중요성, 결정성 위배 – 비타
  - 우리팀의 CI/CD – 칼리

- [2주차 (8월 10일)](#week-2)
  - 우리 서비스에 맞는 이메일 서버 구축기 – 새로이
  - 로깅 전략 수정하기 – 메이
  - OIDC 기반 소셜로그인 연동 – 모코
  - 쿼리 튜닝으로 218배 빨라진 팬 점유율 API – 밍트

- [3주차 (8월 24일)](#week-3)
  - 런칭데이 대비 처리율 제한기 및 로드밸런서 적용기 – 투다
  - 데이터베이스 운영 / 안정성 – 칼리

- [4주차 (9월 07일)](#week-4)
  - 검색 기능 개선 실험하기 – 메이
  - 우리 팀의 TRACES 도입기 – 새로이
  - 야구보구에서 경기 결과를 빠르고 효율적으로 가져오는 방법 – 밍트
  - 테이블 스키마 무중단으로 변경하기 – 모코

- [5주차 (9월 21일)](#week-5)
  - 복구와 안전성을 위한 배포 전략 – 비타
  - FCM & 알림 도메인 – 칼리
  - DB 분산락도 락이다 – 투다

- [6주차 (10월 5일)](#week-6)
  - 웹 크롤러 성능 및 안정성 개선 – 밍트
  - 모니터링 이사하기 CloudWatch에서 Grafana로 – 메이
  - 서비스 무중단으로 테이블 스키마 변경하기 – 모코
  - 우리 팀에 어울리는 검색 기능 도입 과정 1 – 새로이

- [7주차 (10월 19일)](#week-7)
  - 동시성 제어 – 비타
  - FCM 대량 알림 최적화 – 칼리
  - 최종적 일관성 제공하기 – 투다

- [8주차 (11월 02일)](#week-8)
  - 미래의 나를 위한 데이터 파이프라인 설계하기 – 밍트
  - k6 부하테스트와 튜닝을 통한 서버 성능 개선 – 메이
  - 이미지 로딩 최적화 – 모코
  - 우리 서비스, 동시성 문제 이렇게 풀었어요 – 새로이

- [9주차 (11월 16일)](#week-9)
  - GC의 흐름으로 읽는 배치 처리 효율화 – 칼리
  - 알림 아키텍쳐 개선기 – 투다



<br>
<br>

<a id="week-1"></a>
## **1주차** ( 7월 27일 )       

> | 21일간의 리딩 실험하기 | 모니터링 | 테스트 환경의 중요성, 결정성 위배 | 우리팀의 CI/CD |
> | :-:| :-: | :-: | :-: |
> | 밍트 | 투다 | 비타 | 칼리 | 
   
### 💎 발표자료

<img width="2000" height="1125" alt="image" src="https://github.com/user-attachments/assets/980937df-3ba4-4cea-beae-506c5c3228d8" />| <img width="2000" height="1125" alt="image" src="https://github.com/user-attachments/assets/563351c7-a8bf-4854-9219-8aa07960dff4" />
| :---: | :---: |
|[📚 21일간의 리딩 실험하기] <br> [🎥 1주차 발표 영상 - 밍트] |  [📚 모니터링] <br> [🎥 1주차 발표 영상 - 투다] |
<img width="2000" height="1125" alt="image" src="https://github.com/user-attachments/assets/c937aaf3-1f5e-424e-8557-c66518d9016d" /> | <img width="2000" height="1125" alt="image" src="https://github.com/user-attachments/assets/b005b6b5-2c0a-4c95-8630-b38fbd78900b" />
|[📚 테스트 환경의 중요성, 결정성 위배] <br> [🎥 1주차 발표 영상 - 비타] | [📚 우리팀의 CI/CD] <br> [🎥 1주차 발표 영상 - 칼리] |

[📚 21일간의 리딩 실험하기]: https://github.com/woowacourse-study/2025-troubleshooting/blob/main/01_%EC%A3%BC%EC%B0%A8/%E1%84%85%E1%85%B5%E1%84%83%E1%85%B5%E1%86%BC_%E1%84%89%E1%85%B5%E1%86%AF%E1%84%92%E1%85%A5%E1%86%B7%E1%84%92%E1%85%A1%E1%84%80%E1%85%B5(%E1%84%86%E1%85%B5%E1%86%BC%E1%84%90%E1%85%B3).pdf
[🎥 1주차 발표 영상 - 밍트]: https://www.youtube.com/watch?v=L60xNF3kqaY

[📚 모니터링]: https://github.com/woowacourse-study/2025-troubleshooting/blob/main/01_%EC%A3%BC%EC%B0%A8/%E1%84%86%E1%85%A9%E1%84%82%E1%85%B5%E1%84%90%E1%85%A5%E1%84%85%E1%85%B5%E1%86%BC.pdf
[🎥 1주차 발표 영상 - 투다]: https://www.youtube.com/watch?v=wFnjf_T3i8o

[📚 테스트 환경의 중요성, 결정성 위배]: https://github.com/woowacourse-study/2025-troubleshooting/blob/main/01_%EC%A3%BC%EC%B0%A8/%E1%84%90%E1%85%A6%E1%84%89%E1%85%B3%E1%84%90%E1%85%B3%20%E1%84%92%E1%85%AA%E1%86%AB%E1%84%80%E1%85%A7%E1%86%BC%E1%84%8B%E1%85%B4%20%E1%84%8C%E1%85%AE%E1%86%BC%E1%84%8B%E1%85%AD%E1%84%89%E1%85%A5%E1%86%BC%2C%20%E1%84%80%E1%85%A7%E1%86%AF%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%89%E1%85%A5%E1%86%BC%20%E1%84%8B%E1%85%B1%E1%84%87%E1%85%A2(%E1%84%87%E1%85%B5%E1%84%90%E1%85%A1).pdf
[🎥 1주차 발표 영상 - 비타]: https://www.youtube.com/watch?v=dWh_2_KiMGY

[📚 우리팀의 CI/CD]: https://github.com/woowacourse-study/2025-troubleshooting/blob/main/01_%EC%A3%BC%EC%B0%A8/%E1%84%90%E1%85%B3%E1%84%85%E1%85%A5%E1%84%87%E1%85%B3%E1%86%AF%E1%84%89%E1%85%B2%E1%84%90%E1%85%B5%E1%86%BC-CI%3ACD.pdf
[🎥 1주차 발표 영상 - 칼리]: https://youtu.be/cmQxrtBttj0?si=f72MXnLegpscYKEK

---
<br>

<a id="week-2"></a>
## **2주차** ( 8월 10일 )       

> | 우리 서비스에 맞는 이메일 서버 구축기 | 로깅 전략 수정하기 | OIDC 기반 소셜로그인 연동 | 쿼리 튜닝으로 218배 빨라진 팬 점유율 API |
> | :-:| :-: | :-: | :-: |
> | 새로이 | 메이 | 모코 | 밍트 | 
   
### 💎 발표자료

<img width="2000" height="1125" alt="image" src="https://github.com/user-attachments/assets/6243e8f8-f287-4602-9620-18c7cfc06332" />| <img width="2000" height="1125" alt="image" src="https://github.com/user-attachments/assets/fffb84c9-79f7-4d19-b661-ba5a6473f18b" />
| :---: | :---: |
|[📚 우리 서비스에 맞는 이메일 서버 구축기] <br> [🎥 2주차 발표 영상 - 새로이] |  [📚 로깅 전략 수정하기] <br> [🎥 2주차 발표 영상 - 메이] |
<img width="2000" height="1125" alt="image" src="https://github.com/user-attachments/assets/cdeb81db-ace7-4fcc-b659-3929e50a2be6" /> | <img width="2000" height="1125" alt="image" src="https://github.com/user-attachments/assets/2ce14595-a60f-4316-9dba-9c40749adb18" />
|[📚 OIDC 기반 소셜로그인 연동] <br> [🎥 2주차 발표 영상 - 모코] | [📚 쿼리 튜닝으로 218배 빨라진 팬 점유율 API] <br> [🎥 2주차 발표 영상 - 밍트] |

[📚 우리 서비스에 맞는 이메일 서버 구축기]: https://github.com/woowacourse-study/2025-troubleshooting/blob/main/02_%EC%A3%BC%EC%B0%A8/%5B%E1%84%87%E1%85%A1%E1%86%AF%E1%84%91%E1%85%AD%E1%84%8C%E1%85%A1%E1%84%85%E1%85%AD%5D%E1%84%8B%E1%85%AE%E1%84%85%E1%85%B5_%E1%84%89%E1%85%A5%E1%84%87%E1%85%B5%E1%84%89%E1%85%B3%E1%84%8B%E1%85%A6_%E1%84%86%E1%85%A1%E1%86%BD%E1%84%82%E1%85%B3%E1%86%AB_%E1%84%8B%E1%85%B5%E1%84%86%E1%85%A6%E1%84%8B%E1%85%B5%E1%86%AF_%E1%84%89%E1%85%A5%E1%84%87%E1%85%A5_%E1%84%80%E1%85%AE%E1%84%8E%E1%85%AE%E1%86%A8%E1%84%80%E1%85%B5(%E1%84%89%E1%85%A2%E1%84%85%E1%85%A9%E1%84%8B%E1%85%B5).pdf
[🎥 2주차 발표 영상 - 새로이]: https://www.youtube.com/watch?v=bwhBnJ0vyp4&feature=youtu.be

[📚 로깅 전략 수정하기]: https://github.com/woowacourse-study/2025-troubleshooting/blob/main/02_%EC%A3%BC%EC%B0%A8/%5B%E1%84%87%E1%85%A1%E1%86%AF%E1%84%91%E1%85%AD%E1%84%8C%E1%85%A1%E1%84%85%E1%85%AD%5D%E1%84%85%E1%85%A9%E1%84%80%E1%85%B5%E1%86%BC_%E1%84%8C%E1%85%A5%E1%86%AB%E1%84%85%E1%85%A3%E1%86%A8_%E1%84%89%E1%85%AE%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%92%E1%85%A1%E1%84%80%E1%85%B5(%E1%84%86%E1%85%A6%E1%84%8B%E1%85%B5).pdf
[🎥 2주차 발표 영상 - 메이]: https://youtu.be/BAdtFhKRn8E

[📚 OIDC 기반 소셜로그인 연동]: https://github.com/woowacourse-study/2025-troubleshooting/blob/main/02_%EC%A3%BC%EC%B0%A8/%5B%E1%84%87%E1%85%A1%E1%86%AF%E1%84%91%E1%85%AD%E1%84%8C%E1%85%A1%E1%84%85%E1%85%AD%5DOIDC_%E1%84%80%E1%85%B5%E1%84%87%E1%85%A1%E1%86%AB_%E1%84%89%E1%85%A9%E1%84%89%E1%85%A7%E1%86%AF%E1%84%85%E1%85%A9%E1%84%80%E1%85%B3%E1%84%8B%E1%85%B5%E1%86%AB_%E1%84%8B%E1%85%A7%E1%86%AB%E1%84%83%E1%85%A9%E1%86%BC(%E1%84%86%E1%85%A9%E1%84%8F%E1%85%A9).pdf
[🎥 2주차 발표 영상 - 모코]: https://youtu.be/itaHT8111H8

[📚 쿼리 튜닝으로 218배 빨라진 팬 점유율 API]: https://github.com/woowacourse-study/2025-troubleshooting/blob/main/02_%EC%A3%BC%EC%B0%A8/%EC%BF%BC%EB%A6%AC_%EA%B0%9C%EC%84%A0%ED%95%98%EA%B8%B0(%EB%B0%8D%ED%8A%B8).pdf
[🎥 2주차 발표 영상 - 밍트]: https://youtu.be/UYTYqg8R7_g

---

<br>

<a id="week-3"></a>
## **3주차** ( 8월 24일 )       

> | 런칭데이 대비 처리율 제한기 및 로드밸런서 적용기 | 데이터베이스 운영 / 안정성 |
> | :-:| :-: |
> | 투다 | 칼리 | 
   
### 💎 발표자료

<img width="2000" height="1125" alt="image" src="https://github.com/user-attachments/assets/fb5a71ff-ac4f-459b-881f-72ee67d4ff99" /> | <img width="2000" height="1125" alt="image" src="https://github.com/user-attachments/assets/e8c22297-7d5d-43fc-91bf-20d2ac0bd078" />
| :---: | :---: |
| [📚 런칭데이 대비 처리율 제한기 및 로드밸런서 적용기] <br> [🎥 3주차 발표 영상 - 투다] | [📚 데이터베이스 운영 / 안정성] <br> [🎥 3주차 발표 영상 - 칼리] |

[📚 런칭데이 대비 처리율 제한기 및 로드밸런서 적용기]: https://github.com/woowacourse-study/2025-troubleshooting/blob/main/03_3%EC%A3%BC%EC%B0%A8/%E1%84%90%E1%85%B3%E1%84%85%E1%85%A5%E1%84%87%E1%85%B3%E1%86%AF%E1%84%89%E1%85%B2%E1%84%90%E1%85%B5%E1%86%BC-%E1%84%85%E1%85%A9%E1%84%83%E1%85%B3%E1%84%87%E1%85%A2%E1%86%AF.pdf
[🎥 3주차 발표 영상 - 투다]: https://www.youtube.com/watch?v=JmeMQG4_Moc

[📚 데이터베이스 운영 / 안정성]: https://github.com/woowacourse-study/2025-troubleshooting/blob/main/03_3%EC%A3%BC%EC%B0%A8/%E1%84%90%E1%85%B3%E1%84%85%E1%85%A5%E1%84%87%E1%85%B3%E1%86%AF%E1%84%89%E1%85%B2%E1%84%90%E1%85%B5%E1%86%BC%20-%20DB%20%E1%84%8B%E1%85%AE%E1%86%AB%E1%84%8B%E1%85%A7%E1%86%BC.pdf
[🎥 3주차 발표 영상 - 칼리]: https://www.youtube.com/watch?v=C8n0ONC4-mk

---

<br>

<a id="week-4"></a>
## **4주차** ( 9월 07일 )       

> | 검색 기능 개선 실험하기 | 우리 팀의 TRACES 도입기 | 야구보구에서 경기 결과를 빠르고 효율적으로 가져오는 방법 | 테이블 스키마 무중단으로 변경하기 |
> | :-:| :-: | :-: | :-: |
> | 메이 | 새로이 | 밍트 | 모코 | 
   
### 💎 발표자료

<img width="2000" height="1125" alt="image" src="https://github.com/user-attachments/assets/13d35263-0399-46c5-a193-13c3de7e8dd5" />| <img width="2000" height="1125" alt="image" src="https://github.com/user-attachments/assets/baa2ca1b-cea3-4de0-8b47-400e44d92147" />
| :---: | :---: |
|[📚 검색 기능 개선 실험하기] <br> [🎥 4주차 발표 영상 - 메이] |  [📚 우리 팀의 TRACES 도입기] <br> [🎥 4주차 발표 영상 - 새로이] |
<img width="2000" height="1125" alt="image" src="https://github.com/user-attachments/assets/1db4d44c-9a0a-4a6f-ba23-2abaf49c89ca" /> | <img width="2000" height="1125" alt="image" src="https://github.com/user-attachments/assets/15d6f0fa-fbac-46e0-9ac8-340f14995f8b" />
|[📚 야구보구에서 경기 결과를 빠르고 효율적으로 가져오는 방법] <br> [🎥 4주차 발표 영상 - 밍트] | [📚 테이블 스키마 무중단으로 변경하기] <br> [🎥 4주차 발표 영상 - 모코] |

[📚 검색 기능 개선 실험하기]: https://github.com/woowacourse-study/2025-troubleshooting/blob/main/04_4%EC%A3%BC%EC%B0%A8/%5B%E1%84%87%E1%85%A1%E1%86%AF%E1%84%91%E1%85%AD%E1%84%8C%E1%85%A1%E1%84%85%E1%85%AD%5D%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8_%E1%84%80%E1%85%B5%E1%84%82%E1%85%B3%E1%86%BC_%E1%84%80%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%E1%84%92%E1%85%A1%E1%84%80%E1%85%B5(%E1%84%86%E1%85%A6%E1%84%8B%E1%85%B5).pdf
[🎥 4주차 발표 영상 - 메이]: https://www.youtube.com/watch?v=N6j8uwleHk0

[📚 우리 팀의 TRACES 도입기]: https://github.com/woowacourse-study/2025-troubleshooting/blob/main/04_4%EC%A3%BC%EC%B0%A8/%5B%E1%84%87%E1%85%A1%E1%86%AF%E1%84%91%E1%85%AD%E1%84%8C%E1%85%A1%E1%84%85%E1%85%AD%5Dtrace%E1%84%83%E1%85%A9%E1%84%8B%E1%85%B5%E1%86%B8%E1%84%80%E1%85%B5(%E1%84%89%E1%85%A2%E1%84%85%E1%85%A9%E1%84%8B%E1%85%B5).pdf
[🎥 4주차 발표 영상 - 새로이]: https://www.youtube.com/watch?v=-sHLhuB9p0Y

[📚 야구보구에서 경기 결과를 빠르고 효율적으로 가져오는 방법]: https://github.com/woowacourse-study/2025-troubleshooting/blob/main/04_4%EC%A3%BC%EC%B0%A8/%5B%E1%84%87%E1%85%A1%E1%86%AF%E1%84%91%E1%85%AD%E1%84%8C%E1%85%A1%E1%84%85%E1%85%AD%5D%20%E1%84%8B%E1%85%A3%E1%84%80%E1%85%AE%E1%84%87%E1%85%A9%E1%84%80%E1%85%AE%E1%84%8B%E1%85%A6%E1%84%89%E1%85%A5_%E1%84%80%E1%85%A7%E1%86%BC%E1%84%80%E1%85%B5_%E1%84%80%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%E1%84%85%E1%85%B3%E1%86%AF_%E1%84%88%E1%85%A1%E1%84%85%E1%85%B3%E1%84%80%E1%85%A9_%E1%84%92%E1%85%AD%E1%84%8B%E1%85%B2%E1%86%AF%E1%84%8C%E1%85%A5%E1%86%A8%E1%84%8B%E1%85%B3%E1%84%85%E1%85%A9_%E1%84%80%E1%85%A1%E1%84%8C%E1%85%A7%E1%84%8B%E1%85%A9%E1%84%82%E1%85%B3%E1%86%AB_%E1%84%87%E1%85%A1%E1%86%BC%E1%84%87%E1%85%A5%E1%86%B8(%E1%84%86%E1%85%B5%E1%86%BC%E1%84%90%E1%85%B3).pdf
[🎥 4주차 발표 영상 - 밍트]: https://www.youtube.com/watch?v=ijwvmk8ymTM

[📚 테이블 스키마 무중단으로 변경하기]: https://github.com/woowacourse-study/2025-troubleshooting/blob/main/04_4%EC%A3%BC%EC%B0%A8/%5B%E1%84%87%E1%85%A1%E1%86%AF%E1%84%91%E1%85%AD%E1%84%8C%E1%85%A1%E1%84%85%E1%85%AD%5D%E1%84%90%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%87%E1%85%B3%E1%86%AF_%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B5%E1%84%86%E1%85%A1_%E1%84%86%E1%85%AE%E1%84%8C%E1%85%AE%E1%86%BC%E1%84%83%E1%85%A1%E1%86%AB%E1%84%8B%E1%85%B3%E1%84%85%E1%85%A9_%E1%84%87%E1%85%A7%E1%86%AB%E1%84%80%E1%85%A7%E1%86%BC%E1%84%92%E1%85%A1%E1%84%80%E1%85%B5(%E1%84%86%E1%85%A9%E1%84%8F%E1%85%A9).pdf
[🎥 4주차 발표 영상 - 모코]: https://www.youtube.com/watch?v=8ucMsqtZ_e8

---

<br/>

<a id="week-5"></a>
## **5주차** ( 9월 21일 )       

> | 복구와 안전성을 위한 배포 전략 | FCM & 알림 도메인 | DB 분산락도 락이다 |
> | :-:| :-: | :-: |
> | 비타 | 칼리 | 투다 |
   
### 💎 발표자료

<img width="3840" height="2486" alt="스크린샷 2025-09-21 오후 3 58 22" src="https://github.com/user-attachments/assets/42b9468d-e23d-4ff8-9f3e-fb60f1f25f2c" /> | <img width="2746" height="1544" alt="image (1)" src="https://github.com/user-attachments/assets/ba171461-6ce2-49a0-b1a7-33f886776b6d" />
| :---: | :---: |
|[📚 복구와 안전성을 위한 배포 전략] <br> [🎥 4주차 발표 영상 - 비타] |  [📚 FCM & 알림 도메인] <br> [🎥 4주차 발표 영상 - 칼리] |
<img width="2490" height="1322" alt="image (2)" src="https://github.com/user-attachments/assets/30ac915e-d612-475a-8195-5233f443e179" /> | 
|[📚 DB 분산락도 락이다] <br> [🎥 4주차 발표 영상 - 투다] |

[📚 복구와 안전성을 위한 배포 전략]: https://github.com/woowacourse-study/2025-troubleshooting/blob/main/05_5%EC%A3%BC%EC%B0%A8/%5B%E1%84%87%E1%85%A1%E1%86%AF%E1%84%91%E1%85%AD%E1%84%8C%E1%85%A1%E1%84%85%E1%85%AD%5D%20%E1%84%87%E1%85%A9%E1%86%A8%E1%84%80%E1%85%AE%E1%84%8B%E1%85%AA%20%E1%84%8B%E1%85%A1%E1%86%AB%E1%84%8C%E1%85%A5%E1%86%AB%E1%84%89%E1%85%A5%E1%86%BC%E1%84%8B%E1%85%B3%E1%86%AF%20%E1%84%8B%E1%85%B1%E1%84%92%E1%85%A1%E1%86%AB%20%E1%84%87%E1%85%A2%E1%84%91%E1%85%A9%20%E1%84%8C%E1%85%A5%E1%86%AB%E1%84%85%E1%85%A3%E1%86%A8(%E1%84%87%E1%85%B5%E1%84%90%E1%85%A1).pdf
[🎥 4주차 발표 영상 - 비타]: https://www.youtube.com/watch?v=Ac5wr6SjWH0

[📚 FCM & 알림 도메인]: https://github.com/woowacourse-study/2025-troubleshooting/blob/main/05_5%EC%A3%BC%EC%B0%A8/%E1%84%8F%E1%85%A1%E1%86%AF%E1%84%85%E1%85%B5_fcm.pdf
[🎥 4주차 발표 영상 - 칼리]: https://www.youtube.com/watch?v=nUkQZdRDR0s

[📚 DB 분산락도 락이다]: https://github.com/woowacourse-study/2025-troubleshooting/blob/main/05_5%EC%A3%BC%EC%B0%A8/%E1%84%87%E1%85%AE%E1%86%AB%E1%84%89%E1%85%A1%E1%86%AB%E1%84%85%E1%85%A1%E1%86%A8.pdf
[🎥 4주차 발표 영상 - 투다]: https://www.youtube.com/watch?v=INjLBW1pZY8

---

<br/>

<a id="week-6"></a>
## **6주차** ( 10월 5일 )       

> | 웹 크롤러 성능 및 안정성 개선 | 모니터링 이사하기 CloudWatch에서 Grafana로 | 서비스 무중단으로 테이블 스키마 변경하기 | 우리 팀에 어울리는 검색 기능 도입 과정 1 |
> | :-:| :-: | :-: | :-: |
> | 밍트 | 메이 | 모코 | 새로이 |
   
### 💎 발표자료

<img width="1044" height="589" alt="image" src="https://github.com/user-attachments/assets/12892926-bbd2-4ca5-83cb-e32d67875c1b" />| <img width="2556" height="1442" alt="image" src="https://github.com/user-attachments/assets/e48175af-744d-4b6e-9a27-1fd3801d0ecb" />
| :---: | :---: |
|[📚 웹 크롤러 성능 및 안정성 개선] <br> [🎥 6주차 발표 영상 - 밍트] |  [📚 모니터링 이사하기 CloudWatch에서 Grafana로] <br> [🎥 6주차 발표 영상 - 메이] |
<img width="3840" height="2160" alt="image" src="https://github.com/user-attachments/assets/62828cd6-cdca-4ded-808e-ef7c8ef484d9" /> | <img width="1224" height="670" alt="image" src="https://github.com/user-attachments/assets/df8dd3fc-b930-4a04-b34f-0398ddb8d692" />
|[📚 서비스 무중단으로 테이블 스키마 변경하기] <br> [🎥 6주차 발표 영상 - 모코] | [📚 우리 팀에 어울리는 검색 기능 도입 과정 1] <br> [🎥 6주차 발표 영상 - 새로이] |

[📚 웹 크롤러 성능 및 안정성 개선]: https://github.com/woowacourse-study/2025-troubleshooting/blob/main/06_6%EC%A3%BC%EC%B0%A8/%5B%E1%84%87%E1%85%A1%E1%86%AF%E1%84%91%E1%85%AD%E1%84%8C%E1%85%A1%E1%84%85%E1%85%AD%5D%20%E1%84%8B%E1%85%B0%E1%86%B8_%E1%84%8F%E1%85%B3%E1%84%85%E1%85%A9%E1%86%AF%E1%84%85%E1%85%A5%20%E1%84%89%E1%85%A5%E1%86%BC%E1%84%82%E1%85%B3%E1%86%BC_%E1%84%86%E1%85%B5%E1%86%BE_%E1%84%8B%E1%85%A1%E1%86%AB%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%89%E1%85%A5%E1%86%BC_%E1%84%80%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB(%E1%84%86%E1%85%B5%E1%86%BC%E1%84%90%E1%85%B3).pdf
[🎥 6주차 발표 영상 - 밍트]: https://youtu.be/K45Qgg_RKQg?si=-9ge_su6KBSO8ix9

[📚 모니터링 이사하기 CloudWatch에서 Grafana로]: https://github.com/woowacourse-study/2025-troubleshooting/blob/main/06_6%EC%A3%BC%EC%B0%A8/%5B%E1%84%87%E1%85%A1%E1%86%AF%E1%84%91%E1%85%AD%E1%84%8C%E1%85%A1%E1%84%85%E1%85%AD%5D%E1%84%86%E1%85%A9%E1%84%82%E1%85%B5%E1%84%90%E1%85%A5%E1%84%85%E1%85%B5%E1%86%BC_%E1%84%8B%E1%85%B5%E1%84%89%E1%85%A1%E1%84%92%E1%85%A1%E1%84%80%E1%85%B5_CloudWatch%E1%84%8B%E1%85%A6%E1%84%89%E1%85%A5_Grafana%E1%84%85%E1%85%A9(%E1%84%86%E1%85%A6%E1%84%8B%E1%85%B5).pdf
[🎥 6주차 발표 영상 - 메이]: https://www.youtube.com/watch?v=Wge0nSKAymo

[📚 서비스 무중단으로 테이블 스키마 변경하기]: https://github.com/woowacourse-study/2025-troubleshooting/blob/main/06_6%EC%A3%BC%EC%B0%A8/%5B%E1%84%87%E1%85%A1%E1%86%AF%E1%84%91%E1%85%AD%E1%84%8C%E1%85%A1%E1%84%85%E1%85%AD%5D%E1%84%89%E1%85%A5%E1%84%87%E1%85%B5%E1%84%89%E1%85%B3_%E1%84%86%E1%85%AE%E1%84%8C%E1%85%AE%E1%86%BC%E1%84%83%E1%85%A1%E1%86%AB%E1%84%8B%E1%85%B3%E1%84%85%E1%85%A9_%E1%84%90%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%87%E1%85%B3%E1%86%AF_%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B5%E1%84%86%E1%85%A1_%E1%84%87%E1%85%A7%E1%86%AB%E1%84%80%E1%85%A7%E1%86%BC%E1%84%92%E1%85%A1%E1%84%80%E1%85%B5(%E1%84%86%E1%85%A9%E1%84%8F%E1%85%A9).pdf
[🎥 6주차 발표 영상 - 모코]: https://www.youtube.com/watch?v=CP7eR82bXOg

[📚 우리 팀에 어울리는 검색 기능 도입 과정 1]: https://github.com/woowacourse-study/2025-troubleshooting/blob/main/06_6%EC%A3%BC%EC%B0%A8/%5B%E1%84%87%E1%85%A1%E1%86%AF%E1%84%91%E1%85%AD%E1%84%8C%E1%85%A1%E1%84%85%E1%85%AD%5D%E1%84%8B%E1%85%AE%E1%84%85%E1%85%B5_%E1%84%8B%E1%85%A5%E1%84%8B%E1%85%AE%E1%86%AF%E1%84%85%E1%85%B5%E1%84%82%E1%85%B3%E1%86%AB_%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8_%E1%84%80%E1%85%B5%E1%84%82%E1%85%B3%E1%86%BC_%E1%84%83%E1%85%A9%E1%84%8B%E1%85%B5%E1%86%B8_%E1%84%80%E1%85%AA%E1%84%8C%E1%85%A5%E1%86%BC_1(%E1%84%89%E1%85%A2%E1%84%85%E1%85%A9%E1%84%8B%E1%85%B5).pdf
[🎥 6주차 발표 영상 - 새로이]: https://youtu.be/5jIfUgXnx1Y?si=C4xDKwmC28VmGmQ1

---

<br/>

<a id="week-7"></a>
## **7주차** ( 10월 19일 )       

> | 동시성 제어 | FCM 대량 알림 최적화 | 최종적 일관성 제공하기 |
> | :-:| :-: | :-: |
> | 비타 | 칼리 | 투다 |
   
### 💎 발표자료

<img width="2672" height="1494" alt="image (5)" src="https://github.com/user-attachments/assets/e55c7c69-2cf9-447b-9551-dcfca2c1bd4a" /> | <img width="2122" height="1200" alt="image (4)" src="https://github.com/user-attachments/assets/0ffd3c2d-4fbf-44fc-8c1e-1203ace0d377" />
| :---: | :---: |
|[📚 동시성 제어] <br> [🎥 7주차 발표 영상 - 비타] |  [📚 FCM 대량 알림 최적화] <br> [🎥 7주차 발표 영상 - 칼리] |
<img width="3530" height="1876" alt="image (3)" src="https://github.com/user-attachments/assets/328b9d0a-baec-45d5-93d6-5d57979939bd" /> | 
|[📚 최종적 일관성 제공하기] <br> [🎥 7주차 발표 영상 - 투다] |

[📚 동시성 제어]: https://github.com/woowacourse-study/2025-troubleshooting/blob/main/07_7%EC%A3%BC%EC%B0%A8/%E1%84%83%E1%85%A9%E1%86%BC%E1%84%89%E1%85%B5%E1%84%89%E1%85%A5%E1%86%BC%20%E1%84%8C%E1%85%A6%E1%84%8B%E1%85%A5(%E1%84%87%E1%85%B5%E1%84%90%E1%85%A1).pdf
[🎥 7주차 발표 영상 - 비타]: https://youtu.be/xTgy2rSFMtM?si=-2TyzwB0knyRLMeT

[📚 FCM 대량 알림 최적화]: https://github.com/woowacourse-study/2025-troubleshooting/blob/main/07_7%EC%A3%BC%EC%B0%A8/%E1%84%90%E1%85%B3%E1%84%85%E1%85%A5%E1%84%87%E1%85%B3%E1%86%AF%E1%84%89%E1%85%B2%E1%84%90%E1%85%B5%E1%86%BC%20-%20%E1%84%83%E1%85%A2%E1%84%85%E1%85%A3%E1%86%BC%20%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%E1%84%8B%E1%85%AA%20FCM.pdf
[🎥 7주차 발표 영상 - 칼리]: https://youtu.be/CUic_5ZpWOU?si=ukwaWTzbS14CVFI8

[📚 최종적 일관성 제공하기]: https://github.com/woowacourse-study/2025-troubleshooting/blob/main/07_7%EC%A3%BC%EC%B0%A8/%E1%84%90%E1%85%AE%E1%84%83%E1%85%A1%E1%84%90%E1%85%B3%E1%84%85%E1%85%A2%E1%86%AB%E1%84%8C%E1%85%A2%E1%86%A8%E1%84%89%E1%85%A7%E1%86%AB_%E1%84%8B%E1%85%A1%E1%84%8B%E1%85%AE%E1%86%BA%E1%84%87%E1%85%A1%E1%86%A8%E1%84%89%E1%85%B3.pdf
[🎥 7주차 발표 영상 - 투다]: https://youtu.be/ETijlbeb4m8?si=Kwa5NBl_cp3HMtm6

---

<br/>

<a id="week-8"></a>
## **8주차** ( 11월 02일 )       

> | 미래의 나를 위한 데이터 파이프라인 설계하기 | k6 부하테스트와 튜닝을 통한 서버 성능 개선 | 이미지 로딩 최적화 | 우리 서비스, 동시성 문제 이렇게 풀었어요 |
> | :-:| :-: | :-: | :-: |
> | 밍트 | 메이 | 모코 | 새로이 |


### 💎 발표자료

<img width="2082" height="1164" alt="image" src="https://github.com/user-attachments/assets/fbe8f4ac-3cd4-43e9-a432-6d1ae3dea801" /> | <img width="2546" height="1434" alt="image" src="https://github.com/user-attachments/assets/7849caa4-fbe0-4f14-b1ff-2d487ce2abdf" />
| :---: | :---: |
|[📚 미래의 나를 위한 데이터 파이프라인 설계하기] <br> [🎥 8주차 발표 영상 - 밍트] |  [📚 k6 부하테스트와 튜닝을 통한 서버 성능 개선] <br> [🎥 8주차 발표 영상 - 메이] |
<img width="3840" height="2160" alt="image" src="https://github.com/user-attachments/assets/25f06390-0a14-4bd1-9fca-c1c7b20fc52b" /> | <img width="2608" height="1396" alt="image" src="https://github.com/user-attachments/assets/785ad4e8-2310-4072-95c7-286435fb9ef4" />
|[📚 이미지 로딩 최적화] <br> [🎥 8주차 발표 영상 - 모코] | [📚 우리 서비스, 동시성 문제 이렇게 풀었어요] <br> [🎥 8주차 발표 영상 - 새로이] |

[📚 미래의 나를 위한 데이터 파이프라인 설계하기]: https://github.com/woowacourse-study/2025-troubleshooting/blob/main/08_8%EC%A3%BC%EC%B0%A8/%5B%E1%84%87%E1%85%A1%E1%86%AF%E1%84%91%E1%85%AD%E1%84%8C%E1%85%A1%E1%84%85%E1%85%AD%5D%E1%84%86%E1%85%B5%E1%84%85%E1%85%A2%E1%84%8B%E1%85%B4_%E1%84%82%E1%85%A1%E1%84%85%E1%85%B3%E1%86%AF_%E1%84%8B%E1%85%B1%E1%84%92%E1%85%A1%E1%86%AB_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5_%E1%84%91%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%91%E1%85%B3%E1%84%85%E1%85%A1%E1%84%8B%E1%85%B5%E1%86%AB_%E1%84%89%E1%85%A5%E1%86%AF%E1%84%80%E1%85%A8%E1%84%92%E1%85%A1%E1%84%80%E1%85%B5(%E1%84%86%E1%85%B5%E1%86%BC%E1%84%90%E1%85%B3).pdf
[🎥 8주차 발표 영상 - 밍트]: https://www.youtube.com/watch?v=LqsRKoIBw7o

[📚 k6 부하테스트와 튜닝을 통한 서버 성능 개선]: https://github.com/woowacourse-study/2025-troubleshooting/blob/main/08_8%EC%A3%BC%EC%B0%A8/%5B%E1%84%87%E1%85%A1%E1%86%AF%E1%84%91%E1%85%AD%E1%84%8C%E1%85%A1%E1%84%85%E1%85%AD%5Dk6_%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%90%E1%85%A6%E1%84%89%E1%85%B3%E1%84%90%E1%85%B3%E1%84%8B%E1%85%AA_%E1%84%90%E1%85%B2%E1%84%82%E1%85%B5%E1%86%BC%E1%84%8B%E1%85%B3%E1%86%AF_%E1%84%90%E1%85%A9%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB_%E1%84%89%E1%85%A5%E1%84%87%E1%85%A5_%E1%84%89%E1%85%A5%E1%86%BC%E1%84%82%E1%85%B3%E1%86%BC_%E1%84%80%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB.pdf
[🎥 8주차 발표 영상 - 메이]: https://www.youtube.com/watch?v=ODh0-0UiH4A

[📚 이미지 로딩 최적화]: https://github.com/woowacourse-study/2025-troubleshooting/blob/main/08_8%EC%A3%BC%EC%B0%A8/%5B%E1%84%87%E1%85%A1%E1%86%AF%E1%84%91%E1%85%AD%E1%84%8C%E1%85%A1%E1%84%85%E1%85%AD%5D%E1%84%8B%E1%85%B5%E1%84%86%E1%85%B5%E1%84%8C%E1%85%B5_%E1%84%85%E1%85%A9%E1%84%83%E1%85%B5%E1%86%BC_%E1%84%8E%E1%85%AC%E1%84%8C%E1%85%A5%E1%86%A8%E1%84%92%E1%85%AA(%E1%84%86%E1%85%A9%E1%84%8F%E1%85%A9).pdf
[🎥 8주차 발표 영상 - 모코]: https://www.youtube.com/watch?v=eW7U_KFII2c

[📚 우리 서비스, 동시성 문제 이렇게 풀었어요]: https://github.com/woowacourse-study/2025-troubleshooting/blob/main/08_8%EC%A3%BC%EC%B0%A8/%5B%E1%84%87%E1%85%A1%E1%86%AF%E1%84%91%E1%85%AD%E1%84%8C%E1%85%A1%E1%84%85%E1%85%AD%5D%E1%84%8B%E1%85%AE%E1%84%85%E1%85%B5_%E1%84%89%E1%85%A5%E1%84%87%E1%85%B5%E1%84%89%E1%85%B3_%E1%84%83%E1%85%A9%E1%86%BC%E1%84%89%E1%85%B5%E1%84%89%E1%85%A5%E1%86%BC_%E1%84%86%E1%85%AE%E1%86%AB%E1%84%8C%E1%85%A6_%E1%84%8B%E1%85%B5%E1%84%85%E1%85%A5%E1%87%82%E1%84%80%E1%85%A6_%E1%84%91%E1%85%AE%E1%86%AF%E1%84%8B%E1%85%A5%E1%86%BB%E1%84%8B%E1%85%A5%E1%84%8B%E1%85%AD(%E1%84%89%E1%85%A2%E1%84%85%E1%85%A9%E1%84%8B%E1%85%B5).pdf
[🎥 8주차 발표 영상 - 새로이]:https://www.youtube.com/watch?v=Xk3MqkAmBuo

---

<br/>

<a id="week-9"></a>
## **9주차** ( 11월 16일 )       

> | GC의 흐름으로 읽는 배치 처리 효율화 | 알림 아키텍쳐 개선기 |
> | :-:| :-: |
> | 칼리 | 투다 |


### 💎 발표자료

<img width="2082" height="1164" alt="image" src="https://github.com/user-attachments/assets/34fa9972-3419-40f9-b663-cb6f8c743dd1" /> | <img width="2546" height="1434" alt="image" src="https://github.com/user-attachments/assets/1c19ae4c-6b69-4e69-94a1-6124bd4e5ca8" />
| :---: | :---: |
|[📚 GC의 흐름으로 읽는 배치 처리 효율화] <br> [🎥 9주차 발표 영상 - 칼리] |  [📚 알림 아키텍쳐 개선기] <br> [🎥 9주차 발표 영상 - 투다] |

[📚 GC의 흐름으로 읽는 배치 처리 효율화]: https://github.com/woowacourse-study/2025-troubleshooting/blob/main/09_9%EC%A3%BC%EC%B0%A8/%E1%84%90%E1%85%B3%E1%84%85%E1%85%A5%E1%84%87%E1%85%B3%E1%86%AF%E1%84%89%E1%85%B2%E1%84%90%E1%85%B5%E1%86%BC-OOM%E1%84%80%E1%85%AA%20GC.pdf
<!-- [🎥 9주차 발표 영상 - 칼리]: -->

[📚 알림 아키텍쳐 개선기]: https://github.com/woowacourse-study/2025-troubleshooting/blob/main/09_9%EC%A3%BC%EC%B0%A8/%5B%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C%5D%ED%88%AC%EB%8B%A4_%E1%84%8B%E1%85%A1%E1%86%AF%E1%84%85%E1%85%B5%E1%86%B7_%E1%84%8B%E1%85%A1%E1%84%8F%E1%85%B5%E1%84%90%E1%85%A6%E1%86%A8%E1%84%8E%E1%85%A7_%E1%84%80%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB.pdf
<!-- [🎥 9주차 발표 영상 - 투다]: -->

---

<br/>

<a id="week-11"></a>
## **11주차** ( 12월 17일 )       

> | MMMQ 1 BlockingQueue 파헤치기 | DTO Projection과 복합 인덱스로 제거한 936K Range Scan | 재시도 DLQ |
> | :-:| :-: | :-: |
> | 모코 | 칼리 | 투다 |

### 💎 발표자료

<img width="3840" height="2160" alt="image" src="https://github.com/user-attachments/assets/4757c9e4-454f-45b6-b28b-d09023fbb623" /> | <img width="2092" height="1174" alt="image" src="https://github.com/user-attachments/assets/09dbfd0f-97be-47ef-bc54-97559feb5240" />
| :---: | :---: |
|[📚 MMMQ 1 BlockingQueue 파헤치기] <br> [🎥 11주차 발표 영상 - 모코] |  [📚 DTO Projection과 복합 인덱스로 제거한 936K Range Scan] <br> [🎥 11주차 발표 영상 - 칼리] |
<img width="3266" height="1810" alt="image" src="https://github.com/user-attachments/assets/73f50575-d8b9-443c-b640-0b5fa9667170" /> | 
|[📚 재시도 DLQ] <br> [🎥 11주차 발표 영상 - 투다] |

[📚 MMMQ 1 BlockingQueue 파헤치기]: https://github.com/woowacourse-study/2025-troubleshooting/blob/main/11_11%EC%A3%BC%EC%B0%A8/%5B%E1%84%87%E1%85%A1%E1%86%AF%E1%84%91%E1%85%AD%E1%84%8C%E1%85%A1%E1%84%85%E1%85%AD%5DMMMQ_1_BlockingQueue_%E1%84%91%E1%85%A1%E1%84%92%E1%85%A6%E1%84%8E%E1%85%B5%E1%84%80%E1%85%B5(%E1%84%86%E1%85%A9%E1%84%8F%E1%85%A9).pdf
[🎥 11주차 발표 영상 - 모코]: 

[📚 DTO Projection과 복합 인덱스로 제거한 936K Range Scan]: https://github.com/woowacourse-study/2025-troubleshooting/blob/main/11_11%EC%A3%BC%EC%B0%A8/%5B%E1%84%87%E1%85%A1%E1%86%AF%E1%84%91%E1%85%AD%E1%84%8C%E1%85%A1%E1%84%85%E1%85%AD%5D%20DTO_Projection%E1%84%80%E1%85%AA_%E1%84%87%E1%85%A9%E1%86%A8%E1%84%92%E1%85%A1%E1%86%B8_%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%83%E1%85%A6%E1%86%A8%E1%84%89%E1%85%B3%E1%84%85%E1%85%A9_%E1%84%8C%E1%85%A6%E1%84%80%E1%85%A5%E1%84%92%E1%85%A1%E1%86%AB_936K_Range_Scan(%E1%84%8F%E1%85%A1%E1%86%AF%E1%84%85%E1%85%B5).pdf
[🎥 11주차 발표 영상 - 칼리]: 

[📚 재시도 DLQ]: https://github.com/woowacourse-study/2025-troubleshooting/blob/main/11_11%EC%A3%BC%EC%B0%A8/%5B%E1%84%87%E1%85%A1%E1%86%AF%E1%84%91%E1%85%AD%E1%84%8C%E1%85%A1%E1%84%85%E1%85%AD%5D%E1%84%8C%E1%85%A2%E1%84%89%E1%85%B5%E1%84%83%E1%85%A9_DLQ.pdf
[🎥 11주차 발표 영상 - 투다]: 

---
