def calculate_weakness_score(is_correct, solving_time_sec, attempt_count, mistake_type):
    score = 0

    if not is_correct:
        score += 50

    if solving_time_sec > 180:
        score += 20

    if attempt_count >= 3:
        score += 20

    if mistake_type in ["concept_error", "logic_error"]:
        score += 30
    elif mistake_type == "syntax_error":
        score += 10

    return min(score, 100)


def get_recommendation(score):
    if score >= 80:
        return "개념 복습과 기초 문제 재풀이가 필요합니다."
    elif score >= 50:
        return "유사 문제를 추가로 풀며 오답 유형을 확인하는 것이 좋습니다."
    else:
        return "현재 개념 이해도는 비교적 안정적입니다."


sample_submission = {
    "is_correct": False,
    "solving_time_sec": 240,
    "attempt_count": 3,
    "mistake_type": "concept_error"
}

score = calculate_weakness_score(
    sample_submission["is_correct"],
    sample_submission["solving_time_sec"],
    sample_submission["attempt_count"],
    sample_submission["mistake_type"]
)

recommendation = get_recommendation(score)

print("Weakness Score:", score)
print("Recommendation:", recommendation)
