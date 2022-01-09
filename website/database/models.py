from website.database.db import db
from flask_login import UserMixin


class File(db.Model):
    id = db.Column(db.String(300), primary_key=True)
    name = db.Column(db.String(300), nullable=True)
    link = db.Column(db.String(300), nullable=True)
    mimetype = db.Column(db.String(300), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    numberofdownloads = db.Column(db.Integer, nullable=True)


class PublicFile(db.Model):
    id = db.Column(db.String(300), primary_key=True)
    name = db.Column(db.String(300), nullable=True)
    link = db.Column(db.String(300), nullable=True)
    mimetype = db.Column(db.String(300), nullable=True)
    numberofdownloads = db.Column(db.Integer, nullable=True)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    user = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    surname = db.Column(db.String(150))
    files = db.relationship('File')
