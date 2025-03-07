from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import declarative_base
import os

app = Flask(__name__, static_folder="static")

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, 'ourdb.db')

db = SQLAlchemy(app)

Base = declarative_base()
Base.query = db.session.query_property()

import AAT.routes