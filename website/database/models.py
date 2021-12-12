from website.database.db import db


class File(db.Model):
    id = db.Column(db.String(300), primary_key=True)
    name = db.Column(db.String(300), nullable=True)
    link = db.Column(db.String(300), nullable=True)
    mimetype = db.Column(db.String(300), nullable=True)