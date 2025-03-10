from StatisticsReviewer import app, db
from StatisticsReviewer.models import *

from flask import render_template,jsonify
from StatisticsReviewer.FA import Responses,Attempts
from flask_restful import Api


#create a rest API endpoint
api=Api(app)
#take the class that inherits the resource class and its route
api.add_resource(Responses,"/api/Formative/")#A resource in Flask-RESTful is a class that handles HTTP requests.  
api.add_resource(Attempts,"/api/FormativeAttempt/<int:assessment_id>")

@app.route("/")
def stat_home():
    return render_template('stat_home.html')
@app.route("/canvas")
def canavas():
    return render_template('tryCanvas.html')
@app.route("/charts")
def chart():
    return render_template('tryChart.html')
@app.route("/fsStatistics")
def fs():
    lt=allFA("StatisticsReviewer/testdatabase.db","Assessment")
    print(lt)
    return render_template('fsStatistics.html',assessment_lt=lt)

@app.route("/tryflaskresposne")
def table():
    x={1:'alison'}
    return jsonify(x)