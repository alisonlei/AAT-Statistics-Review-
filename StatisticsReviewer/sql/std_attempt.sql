CREATE TABLE Attempts(
    student_id INTEGER,
    student_name TEXT,
    assessment_id INTEGER,
    assessment_name TEXT,
    attempts INTEGER,
    PRIMARY KEY(student_id,assessment_id),
    FOREIGN KEY(assessment_id) REFERENCES Assessment(Assessment_ID),
    FOREIGN KEY(student_id) REFERENCES Student(student_id)

)