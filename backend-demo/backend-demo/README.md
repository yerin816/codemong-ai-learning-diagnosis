# Backend Demo

이 폴더는 CodeMong의 핵심 백엔드 흐름을 FastAPI 형태로 단순화한 데모입니다.

## 구현된 흐름

1. 문제 목록 조회
2. 사용자 답안 제출
3. 정오답 판정
4. 사용자별 취약 개념 집계

## 주요 엔드포인트

| Method | Endpoint | Description |
|---|---|---|
| GET | `/problems` | 등록된 문제 목록을 조회합니다. |
| POST | `/submit` | 사용자의 답안을 제출하고 정오답을 판정합니다. |
| GET | `/diagnosis/{user_id}` | 사용자의 오답 기록을 기준으로 취약 개념을 반환합니다. |

## 향후 개선 방향

- SQLite 또는 MySQL 연동
- 사용자별 풀이 기록 영구 저장
- 오답 유형 자동 분류
- 생성형 AI 기반 진단 설명 기능 연동
