from flask import Flask,render_template,request,flash,redirect,url_for,session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

with open('config.json', 'r') as c:
    params = json.load(c)["params"]

app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
db = SQLAlchemy(app)


class patient(db.Model):
    adharname = db.Column(db.String(50), primary_key=True,nullable=False)
    password = db.Column(db.String(50), unique=False, nullable=False)
    adharno = db.Column(db.String(12), unique=False, nullable=False)
    father = db.Column(db.String(50), primary_key=True,nullable=False)
    mother = db.Column(db.String(50), primary_key=True, nullable=False)
    gender = db.Column(db.String(10), primary_key=True, nullable=False)
    dob = db.Column(db.String(50), primary_key=True,nullable=False)
    email=db.Column(db.String(50), primary_key=True,nullable=False)
    contact=db.Column(db.String(50), primary_key=True,nullable=False)
    state=db.Column(db.String(50), primary_key=True,nullable=False)
    district=db.Column(db.String(50), primary_key=True,nullable=False)
    address=db.Column(db.String(50), primary_key=True,nullable=False)

class sample_collection(db.Model):
    regno = db.Column(db.String(20), primary_key=True, nullable=False)
    regname = db.Column(db.String(50), unique=False, nullable=False)
    password = db.Column(db.String(50), unique=False, nullable=False)
    state = db.Column(db.String(50), primary_key=True, nullable=False)
    district = db.Column(db.String(50), primary_key=True, nullable=False)
    address = db.Column(db.String(250), primary_key=True, nullable=False)
    email = db.Column(db.String(50), primary_key=True, nullable=False)
    contact = db.Column(db.String(15), primary_key=True, nullable=False)
    worktstart = db.Column(db.String(50), primary_key=True, nullable=False)
    worktend = db.Column(db.String(50), primary_key=True, nullable=False)

class testing_facility(db.Model):
    regno = db.Column(db.String(20), primary_key=True, nullable=False)
    regname = db.Column(db.String(50), unique=False, nullable=False)
    password = db.Column(db.String(50), unique=False, nullable=False)
    state = db.Column(db.String(50), primary_key=True, nullable=False)
    district = db.Column(db.String(50), primary_key=True, nullable=False)
    address = db.Column(db.String(250), primary_key=True, nullable=False)
    email = db.Column(db.String(50), primary_key=True, nullable=False)
    contact = db.Column(db.String(15), primary_key=True, nullable=False)
    notest=db.Column(db.String(11), primary_key=True, nullable=False)