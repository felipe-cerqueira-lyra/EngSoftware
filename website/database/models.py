from website.database.db import db
from flask_login import UserMixin


class File(db.Model):
    id = db.Column(db.String(300), primary_key=True)
    name = db.Column(db.String(300), nullable=True)
    link = db.Column(db.String(300), nullable=True)
    mimetype = db.Column(db.String(300), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    files = db.relationship('File')
