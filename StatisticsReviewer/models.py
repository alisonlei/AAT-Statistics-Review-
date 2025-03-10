# from sqlalchemy import text
# from sqlalchemy import Column, Integer, String, Table, ForeignKey
# from sqlalchemy.orm import Mapped, relationship
# from typing import List

# from StatisticsReviewer import Base

# from sqlalchemy import select

import sqlite3

# class FormativeORM(Base):    
#     __tablename__ = "Assessment"
#     # question_id = Column(Integer, primary_key=True)
#     # question_content = Column(String)
#     # correct_response = Column(Integer)
#     # incorrect_response = Column(Integer)
#     Assessment_ID=Column(Integer, primary_key=True)
#     Teacher_ID =Column(Integer)
#     Assessment_type =Column(Integer)
#     Assessment_name  = Column(String)
#     EX_1=Column(Integer)
#     EX_2 =Column(Integer)
#     EX_3 =Column(Integer)
#     EX_4 =Column(Integer)
#     EX_5 =Column(Integer)
#     EX_6 =Column(Integer)
#     EX_7 =Column(Integer)
#     EX_8 =Column(Integer)
#     EX_9 =Column(Integer)
#     EX_10 =Column(Integer)
       
# class FormativeDAO():
#     def getQuestionRes(db):
#         stm=select(FormativeORM)
#         results=db.session.scalars(stm).all()
#         return results
def allFA(database_path, table_name)->list:
    """Counts the number of rows in a SQLite3 table."""

    try:
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM {table_name}")
        FA_lt = cursor.fetchall()
        print("this is from allFA")
        print(FA_lt)
        conn.close()
        return FA_lt

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None
# lass MovieDAO():
    
#     def MovieById(movieid, db):
        
#         stm = select(MovieORM).where(MovieORM.id == movieid)
        
#         movie = db.session.scalar(stm)
        
#         return movie
    
#     def allMovies(db):
        
#         stm = select(MovieORM)
        
#         movies = db.session.scalars(stm).all()
        
#         return movies
        
    