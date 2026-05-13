from diagnosis_logic import calculate_weakness_score, get_recommendation


def test_high_weakness_score():
    score = calculate_weakness_score(
        is_correct=False,
        solving_time_sec=240,
        attempt_count=3,
        mistake_type="concept_error"
    )

    assert score == 100
    assert get_recommendation(score) == "개념 복습과 기초 문제 재풀이가 필요합니다."


def test_medium_weakness_score():
    score = calculate_weakness_score(
        is_correct=False,
        solving_time_sec=100,
        attempt_count=1,
        mistake_type="syntax_error"
    )

    assert score == 60
    assert get_recommendation(score) == "유사 문제를 추가로 풀며 오답 유형을 확인하는 것이 좋습니다."


def test_low_weakness_score():
    score = calculate_weakness_score(
        is_correct=True,
        solving_time_sec=80,
        attempt_count=1,
        mistake_type="none"
    )

    assert score == 0
    assert get_recommendation(score) == "현재 개념 이해도는 비교적 안정적입니다."
