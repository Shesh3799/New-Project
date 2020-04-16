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


class login(db.Model):
    uid = db.Column(db.String(20), primary_key=True,nullable=False)
    username = db.Column(db.String(50), unique=False, nullable=False)
    password = db.Column(db.String(50), unique=False, nullable=False)

class lab_login(db.Model):
    lid = db.Column(db.String(20), primary_key=True,nullable=False)
    username = db.Column(db.String(50), unique=False, nullable=False)
    password = db.Column(db.String(50), unique=False, nullable=False)

class testlab_login(db.Model):
    tid = db.Column(db.String(20), primary_key=True,nullable=False)
    username = db.Column(db.String(50), unique=False, nullable=False)
    password = db.Column(db.String(50), unique=False, nullable=False)