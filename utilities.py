from flask import Flask,render_template,request,flash,redirect,url_for,session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
import random

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

with open('config.json', 'r') as c:
    params = json.load(c)["params"]

app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
db = SQLAlchemy(app)


class patient(db.Model):
    pid = db.Column(db.String(50), primary_key=True, nullable=False)
    adharname = db.Column(db.String(50), primary_key=True,nullable=False)
    password = db.Column(db.String(50), unique=False, nullable=False)
    adharno = db.Column(db.String(12), unique=False, nullable=False)
    father = db.Column(db.String(50), primary_key=False,nullable=False)
    mother = db.Column(db.String(50), primary_key=False, nullable=False)
    gender = db.Column(db.String(10), primary_key=False, nullable=False)
    dob = db.Column(db.String(50), primary_key=False,nullable=False)
    email=db.Column(db.String(50), primary_key=False,nullable=False)
    contact=db.Column(db.String(50), primary_key=False,nullable=False)
    state=db.Column(db.String(50), primary_key=False,nullable=False)
    district=db.Column(db.String(50), primary_key=False,nullable=False)
    address=db.Column(db.String(50), primary_key=False,nullable=False)
    infection=db.Column(db.String(15), primary_key=False,nullable=False)
    book_stat = db.Column(db.Integer, primary_key=False, nullable=False)
    pincode=db.Column(db.String(6), primary_key=False, nullable=False)

class sample_collection(db.Model):
    regno = db.Column(db.String(20), primary_key=True, nullable=False)
    regname = db.Column(db.String(50), unique=False, nullable=False)
    password = db.Column(db.String(50), unique=False, nullable=False)
    state = db.Column(db.String(50), primary_key=False, nullable=False)
    district = db.Column(db.String(50), primary_key=False, nullable=False)
    address = db.Column(db.String(250), primary_key=False, nullable=False)
    email = db.Column(db.String(50), primary_key=False, nullable=False)
    contact = db.Column(db.String(15), primary_key=False, nullable=False)
    worktstart = db.Column(db.String(50), primary_key=False, nullable=False)
    worktend = db.Column(db.String(50), primary_key=False, nullable=False)
    pincode = db.Column(db.String(6), primary_key=False, nullable=False)

class testing_facility(db.Model):
    regno = db.Column(db.String(20), primary_key=True, nullable=False)
    regname = db.Column(db.String(50), unique=False, nullable=False)
    password = db.Column(db.String(50), unique=False, nullable=False)
    state = db.Column(db.String(50), primary_key=False, nullable=False)
    district = db.Column(db.String(50), primary_key=False, nullable=False)
    address = db.Column(db.String(250), primary_key=False, nullable=False)
    email = db.Column(db.String(50), primary_key=False, nullable=False)
    contact = db.Column(db.String(15), primary_key=False, nullable=False)
    notest=db.Column(db.String(11), primary_key=False, nullable=False)

class bookings(db.Model):
    bid = db.Column(db.Integer, primary_key=True, nullable=True)
    pid = db.Column(db.String(50), unique=True, nullable=True)
    lid = db.Column(db.String(50), unique=True, nullable=True)
    name = db.Column(db.String(50), unique=False, nullable=True)
    contact = db.Column(db.String(50), primary_key=False, nullable=True)
    request_date = db.Column(db.String(50), primary_key=False, nullable=True)
    alloted_date = db.Column(db.String(50), primary_key=False, nullable=True)
    risk = db.Column(db.String(50), primary_key=False, nullable=True)
    status = db.Column(db.Integer, nullable=True)
    sample_status = db.Column(db.Integer, nullable=True)
    result = db.Column(db.Integer, nullable=True)