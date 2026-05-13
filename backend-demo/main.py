from fastapi import FastAPI

app = FastAPI()

problems = [
    {
        "problem_id": 1,
        "concept": "조건문",
        "difficulty": "easy",
        "question": "if문의 기본 구조를 고르시오.",
        "answer": "if condition:"
    },
    {
        "problem_id": 2,
        "concept": "반복문",
        "difficulty": "easy",
        "question": "for문에서 반복 범위를 지정할 때 사용하는 함수는?",
        "answer": "range"
    }
]

submissions = []

@app.get("/")
def root():
    return {"message": "CodeMong API Demo"}

@app.get("/problems")
def get_problems():
    return problems

@app.post("/submit")
def submit_answer(user_id: int, problem_id: int, answer: str):
    problem = next((p for p in problems if p["problem_id"] == problem_id), None)

    if problem is None:
        return {"error": "Problem not found"}

    is_correct = answer == problem["answer"]

    submission = {
        "user_id": user_id,
        "problem_id": problem_id,
        "answer": answer,
        "is_correct": is_correct,
        "concept": problem["concept"]
    }

    submissions.append(submission)

    return {
        "result": "correct" if is_correct else "incorrect",
        "submission": submission
    }

@app.get("/diagnosis/{user_id}")
def get_diagnosis(user_id: int):
    user_submissions = [s for s in submissions if s["user_id"] == user_id]

    if not user_submissions:
        return {"message": "No submissions found"}

    incorrect_concepts = {}

    for submission in user_submissions:
        if not submission["is_correct"]:
            concept = submission["concept"]
            incorrect_concepts[concept] = incorrect_concepts.get(concept, 0) + 1

    return {
        "user_id": user_id,
        "weak_concepts": incorrect_concepts,
        "ai_role": "Explain diagnosis result and suggest next learning steps"
    }
