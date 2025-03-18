from AAT import app, db, Base, session, Session
from AAT.models import *
from flask import Flask, render_template, url_for, jsonify, request, redirect, session

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

@app.route("/myassessments/<Teacher_ID>", methods=["GET", "POST"])
def tchSeeAssessments(Teacher_ID):
    # ACCESS ASSESSMENTS SAVED IN DB
    formatives = AssessmentDAO.allFormAssessments(db)
    summatives = AssessmentDAO.allSumAssessments(db)
    return render_template('tch_see_asmts.html',
                            formatives=formatives,
                            summatives=summatives,
                            Teacher_ID=Teacher_ID)

@app.route("/assessmentbuilder<NewIs0OldisID>/<Teacher_ID>", methods=["GET", "POST"])
def buildAssessment(Teacher_ID,NewIs0OldisID):
    # STORE EXERCISES
    FTBs = ExerciseDAO.allFTBExercises(db)
    MCQs = ExerciseDAO.allMCQExercises(db)

    # STORE AUTOCOMPLETES FOR EDITING OLD ASSESSEMENTS
    if NewIs0OldisID != '0':
        assessment = AssessmentDAO.AssessmentById(NewIs0OldisID, db)
        nameFill = assessment.Assessment_name
        ex1Fill = ExerciseDAO.ExerciseById((assessment.ExID_1),db)
        if assessment.ExID_2:
            ex2Fill = ExerciseDAO.ExerciseById((assessment.ExID_2),db)
        else:
            ex2Fill = ''
        if assessment.ExID_3:
            ex3Fill = ExerciseDAO.ExerciseById((assessment.ExID_3),db)
        else:
            ex3Fill = ''
        if assessment.ExID_4:
            ex4Fill = ExerciseDAO.ExerciseById((assessment.ExID_4),db)
        else:
            ex4Fill = ''
        if assessment.ExID_5:
            ex5Fill = ExerciseDAO.ExerciseById((assessment.ExID_5),db)
        else:
            ex5Fill = ''
        if assessment.ExID_6:
            ex6Fill = ExerciseDAO.ExerciseById((assessment.ExID_6),db)
        else:
            ex6Fill = ''
        if assessment.ExID_7:
            ex7Fill = ExerciseDAO.ExerciseById((assessment.ExID_7),db)
        else:
            ex7Fill = ''
        if assessment.ExID_8:
            ex8Fill = ExerciseDAO.ExerciseById((assessment.ExID_8),db)
        else:
            ex8Fill = ''
        if assessment.ExID_9:
            ex9Fill = ExerciseDAO.ExerciseById((assessment.ExID_9),db)
        else:
            ex9Fill = ''
        if assessment.ExID_10:
            ex10Fill = ExerciseDAO.ExerciseById((assessment.ExID_10),db)
        else:
            ex10Fill = ''
        typeFill = assessment.Set0forSum_1forForm
    else:
        nameFill = ''
        ex1Fill = ''
        ex2Fill = ''
        ex3Fill = ''
        ex4Fill = ''
        ex5Fill = ''
        ex6Fill = ''
        ex7Fill = ''
        ex8Fill = ''
        ex9Fill = ''
        ex10Fill = ''
        typeFill = ''
    
    # VARIABLES FOR CONNECTING TO DB
    Set0forSum_1forForm = None
    Assessment_name = None
    ExID_1 = None
    ExID_2 = None
    ExID_3 = None
    ExID_4 = None
    ExID_5 = None
    ExID_6 = None
    ExID_7 = None
    ExID_8 = None
    ExID_9 = None
    ExID_10 = None
    if request.method=="POST":
        Set0forSum_1forForm = request.form["typeOfAssessment"]
        Assessment_name = request.form["assessmentName"]
        ExID_1 = request.form["exercise1"]
        ExID_2 = request.form["exercise2"]
        ExID_3 = request.form["exercise3"]
        ExID_4 = request.form["exercise4"]
        ExID_5 = request.form["exercise5"]
        ExID_6 = request.form["exercise6"]
        ExID_7 = request.form["exercise7"]
        ExID_8 = request.form["exercise8"]
        ExID_9 = request.form["exercise9"]
        ExID_10 = request.form["exercise10"]

        # WIPE PREVIOUS VERSION IF EDITING
        if NewIs0OldisID != '0':
            obj = db.session.query(AssessmentORM).filter_by(Assessment_ID=NewIs0OldisID).one()
            db.session.delete(obj)
            db.session.commit()
            db.session.close()

        assessmentInput = AssessmentORM(Teacher_ID = Teacher_ID,
                                Set0forSum_1forForm = Set0forSum_1forForm,
                                Assessment_name = Assessment_name,
                                ExID_1 = ExID_1,
                                ExID_2 = ExID_2,
                                ExID_3 = ExID_3,
                                ExID_4 = ExID_4,
                                ExID_5 = ExID_5,
                                ExID_6 = ExID_6,
                                ExID_7 = ExID_7,
                                ExID_8 = ExID_8,
                                ExID_9 = ExID_9,
                                ExID_10 = ExID_10)
        db.session.add(assessmentInput)
        db.session.commit()
        db.session.close()
        return redirect(url_for('tchSeeAssessments', Teacher_ID=Teacher_ID))
    else:
        return render_template('tch_build_asmt.html',
                                        FTBs=FTBs,
                                        MCQs=MCQs,
                                        Teacher_ID=Teacher_ID,                                        
                                        nameFill=nameFill,
                                        ex1Fill=ex1Fill,
                                        ex2Fill=ex2Fill,
                                        ex3Fill=ex3Fill,
                                        ex4Fill=ex4Fill,
                                        ex5Fill=ex5Fill,
                                        ex6Fill=ex6Fill,
                                        ex7Fill=ex7Fill,
                                        ex8Fill=ex8Fill,
                                        ex9Fill=ex9Fill,
                                        ex10Fill=ex10Fill,
                                        typeFill=typeFill
                                        )

@app.route("/deleting_assessment_<Assessment_ID>")
def delAss(Assessment_ID):
    assessment = AssessmentDAO.AssessmentById(Assessment_ID,db)
    obj = db.session.query(AssessmentORM).filter_by(Assessment_ID=Assessment_ID).one()
    db.session.delete(obj)
    db.session.commit()
    db.session.close()
    return redirect(url_for('tchSeeAssessments',Teacher_ID=assessment.Teacher_ID))

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

@app.route("/formative_assessment_<Assessment_ID>/<Student_ID>", methods=["GET", "POST"])
def sitFormAssessment(Assessment_ID,Student_ID):
    # SOURCE ASSESSMENT DETAILS...
    assessment = AssessmentDAO.AssessmentById(Assessment_ID,db)
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
    correctAnswers = []
    for exercise in exercises:
        correctAnswers.append(exercise.Correct_answer)

    # MAKE SPACE FOR FORM DATA
    db.session.query(AttemptORM).delete()
    db.session.commit()
    answerInput1 = AttemptORM(Attempt_ID=1,Exercise_ID=assessment.ExID_1,Student_ID=Student_ID)
    answerInput2 = AttemptORM(Attempt_ID=2,Exercise_ID=assessment.ExID_2,Student_ID=Student_ID)
    answerInput3 = AttemptORM(Attempt_ID=3,Exercise_ID=assessment.ExID_3,Student_ID=Student_ID)
    answerInput4 = AttemptORM(Attempt_ID=4,Exercise_ID=assessment.ExID_4,Student_ID=Student_ID)
    answerInput5 = AttemptORM(Attempt_ID=5,Exercise_ID=assessment.ExID_5,Student_ID=Student_ID)
    answerInput6 = AttemptORM(Attempt_ID=6,Exercise_ID=assessment.ExID_6,Student_ID=Student_ID)
    answerInput7 = AttemptORM(Attempt_ID=7,Exercise_ID=assessment.ExID_7,Student_ID=Student_ID)
    answerInput8 = AttemptORM(Attempt_ID=8,Exercise_ID=assessment.ExID_8,Student_ID=Student_ID)
    answerInput9 = AttemptORM(Attempt_ID=9,Exercise_ID=assessment.ExID_9,Student_ID=Student_ID)
    answerInput10 = AttemptORM(Attempt_ID=10,Exercise_ID=assessment.ExID_10,Student_ID=Student_ID)
    db.session.add_all([answerInput1, answerInput2, answerInput3, answerInput4, answerInput5, answerInput6, answerInput7, answerInput8, answerInput9, answerInput10])
    db.session.commit()

    # PROCESS FORM DATA
    if request.method=="POST":
        ans1 = request.form["ans1"]
        if ans1 == correctAnswers[0]:
            Set0forWrong1forRight=1
        else:
            Set0forWrong1forRight=0
        answerInput1.inputtedAnswer = ans1
        answerInput1.Set0forWrong1forRight=Set0forWrong1forRight
        db.session.add(answerInput1)
        db.session.commit()

        ans2 = request.form["ans2"]
        if ans2 == correctAnswers[1]:
            Set0forWrong1forRight=1
        else:
            Set0forWrong1forRight=0
        answerInput2.inputtedAnswer = ans2
        answerInput2.Set0forWrong1forRight=Set0forWrong1forRight
        db.session.add(answerInput2)
        db.session.commit()

        ans3 = request.form["ans3"]
        if ans3 == correctAnswers[2]:
            Set0forWrong1forRight=1
        else:
            Set0forWrong1forRight=0
        answerInput3.inputtedAnswer = ans3
        answerInput3.Set0forWrong1forRight=Set0forWrong1forRight
        db.session.add(answerInput3)
        db.session.commit()

        ans4 = request.form["ans4"]
        if ans4 == correctAnswers[3]:
            Set0forWrong1forRight=1
        else:
            Set0forWrong1forRight=0
        answerInput4.inputtedAnswer = ans4
        answerInput4.Set0forWrong1forRight=Set0forWrong1forRight
        db.session.add(answerInput4)
        db.session.commit()

        ans5 = request.form["ans5"]
        if ans5 == correctAnswers[4]:
            Set0forWrong1forRight=1
        else:
            Set0forWrong1forRight=0
        answerInput5.inputtedAnswer = ans5
        answerInput5.Set0forWrong1forRight=Set0forWrong1forRight
        db.session.add(answerInput5)
        db.session.commit()

        ans6 = request.form["ans6"]
        if ans6 == correctAnswers[5]:
            Set0forWrong1forRight=1
        else:
            Set0forWrong1forRight=0
        answerInput6.inputtedAnswer = ans6
        answerInput6.Set0forWrong1forRight=Set0forWrong1forRight
        db.session.add(answerInput6)
        db.session.commit()

        ans7 = request.form["ans7"]
        if ans7 == correctAnswers[6]:
            Set0forWrong1forRight=1
        else:
            Set0forWrong1forRight=0
        answerInput7.inputtedAnswer = ans7
        answerInput7.Set0forWrong1forRight=Set0forWrong1forRight
        db.session.add(answerInput7)
        db.session.commit()

        ans8 = request.form["ans8"]
        if ans8 == correctAnswers[7]:
            Set0forWrong1forRight=1
        else:
            Set0forWrong1forRight=0
        answerInput8.inputtedAnswer = ans8
        answerInput8.Set0forWrong1forRight=Set0forWrong1forRight
        db.session.add(answerInput8)
        db.session.commit()

        ans9 = request.form["ans9"]
        if ans9 == correctAnswers[8]:
            Set0forWrong1forRight=1
        else:
            Set0forWrong1forRight=0
        answerInput9.inputtedAnswer = ans9
        answerInput9.Set0forWrong1forRight=Set0forWrong1forRight
        db.session.add(answerInput9)
        db.session.commit()

        ans10 = request.form["ans10"]
        if ans10 == correctAnswers[9]:
            Set0forWrong1forRight=1
        else:
            Set0forWrong1forRight=0
        answerInput10.inputtedAnswer = ans10
        answerInput10.Set0forWrong1forRight=Set0forWrong1forRight
        db.session.add(answerInput10)
        db.session.commit()
        
        db.session.close()
        return redirect(url_for('formMark', Assessment_ID=Assessment_ID, Student_ID=1))
    else:
        return render_template('stu_sit_f_asmt.html',assessment=assessment,exercises=exercises)

@app.route("/formative_mark_<Assessment_ID>/<Student_ID>")
def formMark(Assessment_ID,Student_ID):
    # SOURCE ASSESSMENT DETAILS...
    assessment = AssessmentDAO.AssessmentById(Assessment_ID,db)
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
    # SOURCE ATTEMPT INFO...
    pt1 = AttemptDAO.AttemptById(1, db)
    pt2 = AttemptDAO.AttemptById(2, db)
    pt3 = AttemptDAO.AttemptById(3, db)
    pt4 = AttemptDAO.AttemptById(4, db)
    pt5 = AttemptDAO.AttemptById(5, db)
    pt6 = AttemptDAO.AttemptById(6, db)
    pt7 = AttemptDAO.AttemptById(7, db)
    pt8 = AttemptDAO.AttemptById(8, db)
    pt9 = AttemptDAO.AttemptById(9, db)
    pt10 = AttemptDAO.AttemptById(10, db)
    return render_template('stu_f_marks.html',
                        assessment=assessment, 
                        exercises=exercises,
                        pt1=pt1, pt2=pt2, pt3=pt3, pt4=pt4, pt5=pt5,
                        pt6=pt6, pt7=pt7, pt8=pt8, pt9=pt9, pt10=pt10)

@app.route("/formative_feedback_<Assessment_ID>/<Student_ID>")
def formFeedback(Assessment_ID,Student_ID):
    # SOURCE ASSESSMENT DETAILS...
    assessment = AssessmentDAO.AssessmentById(Assessment_ID,db)
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
        
    # SOURCE ATTEMPT INFO...
    pt1 = (AttemptDAO.AttemptById(1, db))
    pt2 = (AttemptDAO.AttemptById(2, db))
    pt3 = (AttemptDAO.AttemptById(3, db))
    pt4 = (AttemptDAO.AttemptById(4, db))
    pt5 = (AttemptDAO.AttemptById(5, db))
    pt6 = (AttemptDAO.AttemptById(6, db))
    pt7 = (AttemptDAO.AttemptById(7, db))
    pt8 = (AttemptDAO.AttemptById(8, db))
    pt9 = (AttemptDAO.AttemptById(9, db))
    pt10 = (AttemptDAO.AttemptById(10, db))
    return render_template('stu_f_fback.html',
                        assessment=assessment, 
                        exercises=exercises,
                        pt1=pt1, pt2=pt2, pt3=pt3, pt4=pt4, pt5=pt5,
                        pt6=pt6, pt7=pt7, pt8=pt8, pt9=pt9, pt10=pt10)

@app.route("/sum_assessment/<Assessment_ID>")
def sitSumAssessment(Assessment_ID):
    return render_template('#')

### END OF STUDENT PAGES ###