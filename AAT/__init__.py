'
# ANYA: I TOOK THIS CODE FROM MY FOP2 SUBMISSION
# I'VE REMOVED A FEW THINGS THAT WEREN'T RELEVANT TO THIS PROJECT
# HOPEFULLY IT STILL WORKS, BUT WE'LL NEED TO CHECK

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import declarative_base
import os

app = Flask(__name__, static_folder="static")

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, 'fileName.db') # Change to our db name

db = SQLAlchemy(app)

Base = declarative_base()
Base.query = db.session.query_property()

import AAT.routes    # Can't remember what this is