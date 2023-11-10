# Information that we need to represent a real world object

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

#initializing the database
db = SQLAlchemy()



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(240), nullable = True)
    title = db.Column(db.String(40), nullable = False)
    img_url = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

class Comment(db.Model):
    id =  db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable = False)

    



    




