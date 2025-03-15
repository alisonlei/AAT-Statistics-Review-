from AAT import app, db
from AAT.models import *
from flask import Flask, render_template, url_for,jsonify,request

# from StatisticsReviewer import app, db
# from StatisticsReviewer.models import *
from Stat_resources import Responses,Attempts,SaScore
from flask_restful import Api
#create a rest API endpoint
api=Api(app)
#take the class that inherits the resource class and its route
api.add_resource(Responses,"/api/Formative/")#A resource in Flask-RESTful is a class that handles HTTP requests.  
api.add_resource(Attempts,"/api/FormativeAttempt/<int:assessment_id>")
api.add_resource(SaScore,"/api/Attainment/<int:assessment_id>/<int:cohort>")



### LANDING PAGE ###
@app.route("/")
def landingPage():
    return render_template('landing.html')



### TEACHER PAGES ###
@app.route("/register/teacher")
def teacherReg():
    return render_template('tch_register.html')

@app.route("/home/<Teacher_ID>")
def teacherHome(Teacher_ID):
    return render_template('tch_home.html',Teacher_ID=Teacher_ID)

@app.route("/myassessments/<Teacher_ID>")
def tchSeeAssessments(Teacher_ID):
    formatives = AssessmentDAO.allFormAssessments(db) #STORE ALL FORMATIVE ASSESSMENT ROWS IN VARIABLE
    summatives = AssessmentDAO.allSumAssessments(db) #STORE ALL SUMMATIVE ASSESSMENT ROWS IN VARIABLE
    return render_template('tch_see_asmts.html',formatives=formatives,summatives=summatives,Teacher_ID=Teacher_ID)

@app.route("/assessmentbuilder/<Teacher_ID>")
def buildAssessment(Teacher_ID):
    FTBs = ExerciseDAO.allFTBExercises(db) #STORE ALL FTB EXERCISE ROWS IN VARIABLE
    MCQs = ExerciseDAO.allMCQExercises(db) #STORE ALL MCQ EXERCISE ROWS IN VARIABLE
    return render_template('tch_build_asmt.html',FTBs=FTBs,MCQs=MCQs,Teacher_ID=Teacher_ID)

@app.route("/teacher/stat_home") 
def stat_home():
    return render_template('stat_home.html')

@app.route("/teacher/stat_home/attainment")
def attainment():
    print("get attainment")
    #this function gets the first summative assessment res for all intake years
    return render_template('tch_statistics/attainment.html')

@app.route("/teacher/stat_home/fs")
def fs():
    assessment_names=getParameters("StatisticsReviewer/testdatabase.db","Assessment","Assessment_name")
    print(assessment_names)
    topics=getParameters("StatisticsReviewer/testdatabase.db","Response","topic")
    return render_template('tch_statistics/fsStatistics.html',assessment_lt=assessment_names,topic_lt=topics)
### END OF TEACHER PAGES ###



### STUDENT PAGES ###
@app.route("/register/student")
def studentReg():
    return render_template('stu_register.html')

@app.route("/search")
def studentHome():
    return render_template('stu_home.html')

@app.route("/teacher/<Teacher_ID>")
def stuSeeAssessments(Teacher_ID):
    formatives = AssessmentDAO.allFormAssessments(db) #STORE ALL FORMATIVE ASSESSMENT ROWS IN VARIABLE
    summatives = AssessmentDAO.allSumAssessments(db) #STORE ALL SUMMATIVE ASSESSMENT ROWS IN VARIABLE
    return render_template('stu_see_asmts.html',formatives=formatives,summatives=summatives,Teacher_ID=Teacher_ID)

@app.route("/form_assessment/<Assessment_ID>")
def sitFormAssessment(Assessment_ID):
    assessment = AssessmentDAO.AssessmentById(Assessment_ID,db)
    # SOURCE DETAILS ON ASSIGNMENT'S EXERCISES...
    exerciseIDs = [
        assessment.ExID_1,
        assessment.ExID_2,
        assessment.ExID_3,
        assessment.ExID_4,
        assessment.ExID_5,
        assessment.ExID_6,
        assessment.ExID_7,
        assessment.ExID_8,
        assessment.ExID_9,
        assessment.ExID_10,
    ]
    exercises = []
    for exerciseID in exerciseIDs:
        exercise = ExerciseDAO.ExerciseById(exerciseID,db)
        exercises.append(exercise)
    # ...END OF SOURCING DETAILS ON ASSIGNMENT'S EXERCISES
    return render_template('stu_sit_f_asmt.html',assessment=assessment,exercises=exercises)

@app.route("/sum_assessment/<Assessment_ID>")
def sitSumAssessment(Assessment_ID):
    return render_template('#')

@app.route("/form_feedback/<Assessment_ID>")
def formFeedback(Assessment_ID):
    assessment = AssessmentDAO.AssessmentById(Assessment_ID,db)
    # SOURCE DETAILS ON ASSIGNMENT'S EXERCISES...
    exerciseIDs = [
        assessment.ExID_1,
        assessment.ExID_2,
        assessment.ExID_3,
        assessment.ExID_4,
        assessment.ExID_5,
        assessment.ExID_6,
        assessment.ExID_7,
        assessment.ExID_8,
        assessment.ExID_9,
        assessment.ExID_10,
    ]
    exercises = []
    for exerciseID in exerciseIDs:
        exercise = ExerciseDAO.ExerciseById(exerciseID,db)
        exercises.append(exercise)
    # ...END OF SOURCING DETAILS ON ASSIGNMENT'S EXERCISES
    return render_template('stu_f_fback.html',exercises=exercises,assessment=assessment)
### END OF STUDENT PAGES ###