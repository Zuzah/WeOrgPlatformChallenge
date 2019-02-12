from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
from settings import app

#SQLAlchemy APIs
db = SQLAlchemy(app)

class Puppy(db.Model):
    __tablename__ = 'puppies'
    post_id = db.Column(db.Integer,primary_key=True)
    user_token = db.Column(db.Integer,primary_key=True)
    date_created = db.Column(db.DateTime,default=datetime.utcnow)
    likes = db.Column(db.Integer)
    img_src = db.Column(db.String(1000), nullable=False)
    message = db.Column(db.String(255), nullable=True)

    #Used to return json version of return results
    def json(self):
        return {
            'post_id': self.post_id,
            'user_token': self.user_token,
            'date_created':self.date_created,
            'likes': self.likes,
            'img_src':self.img_src,
            'message':self.message
        }

    def add_puppy_post(_post_id, _user_token, _date_created, _likes, _img_src, _message ):
        new_post = Puppy(post_id=_post_id, user_token=_user_token, date_created=_date_created, likes=_likes, img_src=_img_src, message=_message)
        db.session.add(new_post)
        db.session.commit()

    #Query to get all posts (represents the photo feed)
    def get_all_puppy_posts():
        #Query all the puppy posts (the feed )
        return Puppy.query.all()

    #Let a user like a Post
    def like_a_post(_post_id):
        post_to_like = Puppy.query.filter_by(post_id=_post_id).first()
        post_to_like.likes+=1
        db.session.commit()

    #To return the above, we define a representation method to do so
    #Below, represent the database return as a json object
    def __repr__(self):
        puppy_post_object = {
            'post_id': self.post_id,
            'user_token': self.user_token,
            'date_created':self.date_created,
            'likes': self.likes,
            'img_src':self.img_src,
            'message':self.message
        }
        return json.dumps(puppy_post_object, indent=4, sort_keys=True, default=str)
