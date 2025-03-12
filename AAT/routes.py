from AAT import app, db
from flask import Flask, render_template, url_for



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
# END OF TEACHER PAGES #



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
# END OF STUDENT PAGES #