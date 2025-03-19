from flask_restful import Resource,reqparse
# from datetime import datetime
# from sqlalchemy import text
# from sqlalchemy import Column, Integer, String, Table, ForeignKey
# from sqlalchemy.orm import Mapped, relationship
# from typing import List
# from StatisticsReviewer import Base,db
# from sqlalchemy import select



# class FormativeORM(Base):    
#     __tablename__ = "Formative"
#     question_id = Column(Integer, primary_key=True)
#     question_content = Column(String)
#     correct_response = Column(Integer)
#     incorrect_response = Column(Integer)
    
# class FormativeDAO():
#     def getQuestionRes(self):
#         stm=select(FormativeORM)
#         results=db.session.scalars(stm).all()
#         return results
    
import sqlite3
from flask import jsonify
def get_db_conn():
    conn = sqlite3.connect('StatisticsReviewer/testdatabase.db')
    conn.row_factory = sqlite3.Row
    return conn



class Responses(Resource):
    def get(self):
        
        conn=get_db_conn()
        res = conn.execute('SELECT * FROM Response').fetchall()
        response_rows=[dict(row) for row in res]#res is a row object which need to be converted to python basic data types
        print(response_rows)
        conn.close()
        
        return jsonify(response_rows)


    def post(self):
        conn=get_db_conn()
        res = conn.execute('SELECT * FROM Response').fetchall()
        response_rows=[dict(row) for row in res]#res is a row object which need to be converted to python basic data types
        print(response_rows)
        conn.close()
        
        return jsonify(response_rows)
class Attempts(Resource):
    def get(self,assessment_id):

        conn=get_db_conn()

        sql='SELECT * FROM Attempts WHERE assessment_id='+str(assessment_id)
        res = conn.execute(sql).fetchall()
        attempt_rows=[dict(row) for row in res]#res is a row object which need to be converted to python basic data types
        print(attempt_rows)
        conn.close()
        
        return jsonify(attempt_rows)

class SaScore(Resource):#table cols:student id,intake year,sa1,sa2...
    def get(self,assessment_id,cohort):

        conn=get_db_conn()
        
        

        sql='SELECT * FROM Summative'
        res= conn.execute(sql).fetchall()
        
        
        selected_assessment_col=assessment_id+1

        if cohort==1:
            res_by_yr={}
            for row in res:
                res_by_yr.setdefault(row[1],[]).append(row[selected_assessment_col])
            
            for intake_yr in res_by_yr:
                res_by_yr[intake_yr].sort()
            print("this is from api ScoreDistribution")
            print(res_by_yr)
            conn.close()
            return jsonify(res_by_yr)
        else:
            print ("this is from stat resource to get indiv result")
            res=[dict(row) for row in res]
            print(res)
            conn.close()
            return jsonify(res)


"""
for reference
class Formative_A(Resource):
    
    def get(self):
        
        conn=get_db_conn()
        res = conn.execute('SELECT * FROM Test').fetchall()
        new=[dict(row) for row in res]#res is a row object which need to be converted to python basic data types
        print(new)
        conn.close()
        
        return jsonify(new)#allow the data to be transferred across the network,serialized?
"""    

####referencing code#####
# import sqlite3
# from flask import Flask, render_template

# app = Flask(__name__)

# def get_db_connection():
#     conn = sqlite3.connect('database.db')
#     conn.row_factory = sqlite3.Row
#     return conn


# @app.route('/')
# def index():
#     conn = get_db_connection()
#     posts = conn.execute('SELECT * FROM posts').fetchall()
#     conn.close()
#     return render_template('index.html', posts=posts)