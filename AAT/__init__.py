from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os

## SQL ALCHEMY STUFF ##
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__, static_folder="static")
app.secret_key = "hello"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, 'database/ourdb.db')
db = SQLAlchemy(app)

## SET UP TO ADD TO DB ##
db_url = "sqlite:///database/ourdb.db"
engine = create_engine(db_url)
Base = declarative_base()
Base.query = db.session.query_property()
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

import AAT.routes