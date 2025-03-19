CREATE TABLE Teacher(
    Teacher_ID INTEGER,
    PRIMARY KEY(Teacher_ID)
);

CREATE TABLE Assessment(
    Assessment_ID INTEGER,
    Teacher_ID INTEGER NOT NULL,
    Set0forSum_1forForm INTEGER NOT NULL,
    Assessment_name TEXT NOT NULL,
    ExID_1 INTEGER,
    ExID_2 INTEGER,
    ExID_3 INTEGER,
    ExID_4 INTEGER,
    ExID_5 INTEGER,
    ExID_6 INTEGER,
    ExID_7 INTEGER,
    ExID_8 INTEGER,
    ExID_9 INTEGER,
    ExID_10 INTEGER,
    PRIMARY KEY(Assessment_ID),
    FOREIGN KEY (Teacher_ID) REFERENCES Assessment(Teacher_ID),
    FOREIGN KEY (ExID_1) REFERENCES Exercise(Exercise_ID),
    FOREIGN KEY (ExID_2) REFERENCES Exercise(Exercise_ID),
    FOREIGN KEY (ExID_3) REFERENCES Exercise(Exercise_ID),
    FOREIGN KEY (ExID_4) REFERENCES Exercise(Exercise_ID),
    FOREIGN KEY (ExID_5) REFERENCES Exercise(Exercise_ID),
    FOREIGN KEY (ExID_6) REFERENCES Exercise(Exercise_ID),
    FOREIGN KEY (ExID_7) REFERENCES Exercise(Exercise_ID),
    FOREIGN KEY (ExID_8) REFERENCES Exercise(Exercise_ID),
    FOREIGN KEY (ExID_9) REFERENCES Exercise(Exercise_ID),
    FOREIGN KEY (ExID_10) REFERENCES Exercise(Exercise_ID)
);

CREATE TABLE Exercise(
    Exercise_ID INTEGER,
    Teacher_ID INTEGER NOT NULL,
    Set0forFTB_1forMCQ INTEGER NOT NULL,
    Topic TEXT NOT NULL,
    Question TEXT NOT NULL,
    Correct_answer TEXT NOT NULL,
    How_corr_answ_was_reached TEXT NOT NULL,
    FalseOp1 TEXT,
    FalseOp2 TEXT,
    FalseOp3 TEXT,
    PRIMARY KEY(Exercise_ID),
    FOREIGN KEY (Teacher_ID) REFERENCES Assessment(Teacher_ID)
);

CREATE TABLE Attempt(
    Attempt_ID INTEGER,
    Exercise_ID INTEGER,
    Student_ID INTEGER,
    inputtedAnswer TEXT,
    Set0forWrong1forRight INTEGER,
    PRIMARY KEY(Attempt_ID)
);