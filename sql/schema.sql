CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(100)
);

CREATE TABLE concepts (
    concept_id INTEGER PRIMARY KEY,
    unit_name VARCHAR(100),
    concept_name VARCHAR(100)
);

CREATE TABLE problems (
    problem_id INTEGER PRIMARY KEY,
    concept_id INTEGER,
    title VARCHAR(200),
    difficulty VARCHAR(20),
    weight INTEGER,
    answer VARCHAR(100),
    FOREIGN KEY (concept_id) REFERENCES concepts(concept_id)
);

CREATE TABLE mistake_types (
    mistake_type_id INTEGER PRIMARY KEY,
    mistake_name VARCHAR(100),
    description TEXT
);

CREATE TABLE submissions (
    submission_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    problem_id INTEGER,
    submitted_answer VARCHAR(100),
    is_correct BOOLEAN,
    mistake_type_id INTEGER,
    solving_time_sec INTEGER,
    attempt_count INTEGER,
    created_at DATETIME,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (problem_id) REFERENCES problems(problem_id),
    FOREIGN KEY (mistake_type_id) REFERENCES mistake_types(mistake_type_id)
);

CREATE TABLE diagnoses (
    diagnosis_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    concept_id INTEGER,
    weakness_score FLOAT,
    recommendation TEXT,
    created_at DATETIME,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (concept_id) REFERENCES concepts(concept_id)
);
