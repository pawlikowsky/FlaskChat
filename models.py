from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://hyupxkudylrnlf:4055f45e208356a9c64af6bb9511a8441d6632b6ef1c30e2550bd4aee29ce08c@ec2-23-23-244-83.compute-1.amazonaws.com:5432/dejhiqa16ncouf'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chat_uid = db.Column(db.String(12), unique=True)
    content = db.Column(db.String)
    editor = db.Column(db.String(12))
    created = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, chat_uid=None, editor='python', content=None):
        self.chat_uid=chat_uid
        self.editor=editor
        self.content=content


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email=None):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username
