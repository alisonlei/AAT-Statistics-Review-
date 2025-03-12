from AAT import app, db
from flask import Flask, render_template, url_for


@app.route("/")
def landingPage():
    return render_template('landing.html')


# TEACHER PAGES #
@app.route("/teacher/register")
def teacherReg():
    return render_template('teach_register.html')

@app.route("/teacher")
def teacherHome():
    return render_template('teach_home.html')

@app.route("/teacher/myassessments")
def teacherMyAssessments():
    return render_template('my_assessments.html')
# END OF TEACHER PAGES #


# STUDENT PAGES #
@app.route("/student/register")
def studentReg():
    return render_template('stu_register.html')

@app.route("/student")
def studentHome():
    return render_template('stu_home.html')
# END OF STUDENT PAGES #