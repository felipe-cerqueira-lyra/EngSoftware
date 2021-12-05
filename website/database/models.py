from website.database.db import db


class Img(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300), nullable=True)
    img = db.Column(db.Text, unique=True, nullable=False)
    mimetype = db.Column(db.Text, nullable=True)
