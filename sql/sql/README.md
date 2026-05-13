# Database Schema

이 폴더는 CodeMong의 학습 진단 기능을 위한 초기 데이터베이스 구조를 정리한 공간입니다.

## 주요 테이블

| Table | Purpose |
| users | 사용자 정보 저장 |
| concepts | 단원 및 개념 정보 저장 |
| problems | 문제 정보 저장 |
| mistake_types | 오답 유형 정보 저장 |
| submissions | 사용자 풀이 기록 저장 |
| diagnoses | 취약 개념 진단 결과 저장 |

## 설계 의도

CodeMong은 단순히 정답 여부만 저장하는 것이 아니라, 사용자의 풀이 과정에서 발생하는 오답 유형, 풀이 시간, 시도 횟수 등을 함께 저장해 취약 개념을 진단하는 구조를 목표로 합니다.
