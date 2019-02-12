from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
from settings import app


db = SQLAlchemy(app)

class Puppy(db.Model):
    __tablename__ = 'puppies'
    post_id = db.Column(db.Integer,primary_key=True)
    user_token = db.Column(db.Integer,primary_key=True)
    data_created = db.Column(db.DateTime,default=datetime.utcnow)
    data_edited = db.Column(db.DateTime, default=datetime.utcnow)
    likes = db.Column(db.Integer)
    img_src = db.Column(db.String(1000), nullable=False)
    message = db.Column(db.String(255), nullable=True)
