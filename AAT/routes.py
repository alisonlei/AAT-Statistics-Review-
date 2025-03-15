from AAT import app, db
from flask import Flask, render_template, url_for,jsonify,request

# from StatisticsReviewer import app, db
# from StatisticsReviewer.models import *

from Stat_resources import Responses,Attempts,SaScore
from flask_restful import Api
from AAT.models import *
#create a rest API endpoint
api=Api(app)
#take the class that inherits the resource class and its route
api.add_resource(Responses,"/api/Formative/")#A resource in Flask-RESTful is a class that handles HTTP requests.  
api.add_resource(Attempts,"/api/FormativeAttempt/<int:assessment_id>")
api.add_resource(SaScore,"/api/Attainment/<int:assessment_id>/<int:cohort>")


@app.route("/")
def landingPage():
    return render_template('landing.html')



# TEACHER PAGES #
@app.route("/teacher/register")
def teacherReg():
    return render_template('tch_register.html')

@app.route("/teacher/home")
def teacherHome():
    return render_template('tch_home.html')

@app.route("/teacher/myassessments") #when we have teacherIDs, change this to /teacher/myassessments/#
def tchSeeAssessments():
    return render_template('tch_see_asmts.html')

@app.route("/teacher/assessmentbuilder") #when we have teacherIDs, change this to /teacher/assessmentbuilder/#
def buildAssessment():
    return render_template('tch_build_asmt.html')

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

#END OF TEACHER PAGES #



# STUDENT PAGES #
@app.route("/student/register")
def studentReg():
    return render_template('stu_register.html')

@app.route("/student/home")
def studentHome():
    return render_template('stu_home.html')

@app.route("/student/assessments") #when we have teacherIDs, change this to /student/assessments/#
def stuSeeAssessments():
    return render_template('stu_see_asmts.html')

@app.route("/student/form_assessment") #when we have assessmentIDs, change this to /student/form_assessment/#
def sitFormAssessment():
    return render_template('stu_sit_f_asmt.html')

@app.route("/student/sum_assessment") #when we have assessmentIDs, change this to /student/sum_assessment/#
def sitSumAssessment():
    return render_template('#') #populate

@app.route("/student/form_feedback") #when we have attemptID, change this to /student/form_feedback/#
def formFeedback():
    return render_template('stu_f_fback.html') #populate

@app.route("/student/sum_feedback") #when we have attemptID, change this to /student/sum_feedback/#
def sumFeedback():
    return render_template('#') #populate
# END OF STUDENT PAGES #