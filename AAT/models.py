from AAT import Base
from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy import select, text
from typing import List




# LINK 'Assessment' AND 'Exercise' TABLES THROUGH 'OBJECT RELATIONSHIP MAPPING'(ORM)
# ASSESSMENT TABLE ORM
class AssessmentORM(Base):    
    __tablename__ = "Assessment"
    Assessment_ID = Column(Integer, primary_key=True)
    Teacher_ID = Column(Integer)
    Set0forSum_1forForm = Column(Integer)
    Assessment_name = Column(String)
    ExID_1 = Column(Integer)
    ExID_2 = Column(Integer)
    ExID_3 = Column(Integer)
    ExID_4 = Column(Integer)
    ExID_5 = Column(Integer)
    ExID_6 = Column(Integer)
    ExID_7 = Column(Integer)
    ExID_8 = Column(Integer)
    ExID_9 = Column(Integer)
    ExID_10 = Column(Integer)
    assessments: Mapped[List["ExerciseORM"]] = relationship(secondary='assessmentContent')
# EXERCISE TABLE ORM
class ExerciseORM(Base):    
    __tablename__ = "Exercise"
    Exercise_ID  = Column(Integer, primary_key=True)
    Teacher_ID  = Column(Integer)
    Set0forFTB_1forMCQ = Column(Integer)
    Topic = Column(String)
    Question = Column(String)
    Correct_answer = Column(String)
    How_corr_answ_was_reached = Column(String)
    FalseOp1 = Column(String)
    FalseOp2 = Column(String)
    FalseOp3 = Column(String)
    exercises: Mapped[List["AssessmentORM"]] = relationship(secondary='assessmentContent')
# DEFINE THE RELATIONSHIP [IF WE NEED TO USE THIS WE NEED TO MAKE TABLE 'assessmentContent']
    assessmentContent = Table(
        'assessmentContent',
        Base.metadata,
        Column("Exercise_ID", ForeignKey("Exercise.Exercise_ID"), primary_key=True),
        Column("Assessment_ID", ForeignKey("Assessment.Assessment_ID"), primary_key=True),
    )




# ACCESS DATA FROM 'Assessment' TABLE THROUGH 'DATA ACCESS OBJECT' (DAO)
class AssessmentDAO():
    def AssessmentById(Assessment_ID, db): #METHOD TO ACCESS AN INDIVIDUAL ASSESSMENT'S ROW
        stm = select(AssessmentORM).where(AssessmentORM.Assessment_ID == Assessment_ID)
        found_assessment = db.session.scalar(stm)
        return found_assessment
    def allFormAssessments(db): #METHOD TO ACCESS ALL FORMATIVE ASSESSMENT ROWS
        found_assessments = db.session.query(AssessmentORM).where(AssessmentORM.Set0forSum_1forForm == 1).all()
        return found_assessments
    def allSumAssessments(db): #METHOD TO ACCESS ALL SUMMATIVE ASSESSMENT ROWS
        found_assessments = db.session.query(AssessmentORM).where(AssessmentORM.Set0forSum_1forForm == 0).all()
        return found_assessments
    def allAssessments(db): #METHOD TO ACCESS ALL 'ASSESSMENT' ROWS
        stm = select(AssessmentORM)
        found_assessments = db.session.scalars(stm).all()
        return found_assessments

# ACCESS DATA FROM 'Exercise' TABLE THROUGH 'DATA ACCESS OBJECT' (DAO)
class ExerciseDAO():
    def ExerciseById(Exercise_ID, db): #METHOD TO ACCESS AN INDIVIDUAL EXERCISE'S ROW
        stm = select(ExerciseORM).where(ExerciseORM.Exercise_ID == Exercise_ID)
        found_exercise = db.session.scalar(stm)
        return found_exercise
    def allFTBExercises(db): #METHOD TO ACCESS ALL FILL THE BLANK EXERCISE ROWS
        found_exercises = db.session.query(ExerciseORM).where(ExerciseORM.Set0forFTB_1forMCQ == 0).all()
        return found_exercises
    def allMCQExercises(db): #METHOD TO ACCESS ALL MULTIPLE CHOICE EXERCISE ROWS
        found_exercises = db.session.query(ExerciseORM).where(ExerciseORM.Set0forFTB_1forMCQ == 1).all()
        return found_exercises
    def allExercises(db): #METHOD TO ACCESS ALL 'EXERCISE' ROWS
        stm = select(ExerciseORM)
        found_exercises = db.session.scalars(stm).all()
        return found_exercises


# STATISTICS
import sqlite3
def queryDb(database_path,table_name,sql):
    try:
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        cursor.execute(sql)
        res=cursor.fetchall()
        print("query result:")
        print(res)
        conn.close()
        return res

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None

def getParameters(database_path, table_name,col_name)->list:
    """Counts the number of rows in a SQLite3 table."""
    res=queryDb(database_path,table_name,f"SELECT  {col_name}  FROM {table_name}")
    formatted_result = [parameter[0] for parameter in res]
    print("after formating")
    print(formatted_result)
    return formatted_result

def getFirstSARes(database_path,table_name):
    try:
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        
        sql='SELECT intake_year,sa1 FROM Summative'
        res= cursor.execute(sql).fetchall()#a list of tuples,each tuple is a row

        res_by_yr={}
        for row in res:
            res_by_yr.setdefault(row[0],[]).append(row[1])
        
        for intake_yr in res_by_yr:
            res_by_yr[intake_yr].sort()
        
        conn.close()
        return res_by_yr

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None
# END OF STATISTICS