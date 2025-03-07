from AAT import app, db
from flask import Flask, render_template, url_for

@app.route("/")
def testPage():
    return render_template('testPage.html')