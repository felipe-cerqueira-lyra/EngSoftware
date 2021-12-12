from website.database.db import db


class File(db.Model):
    id = db.Column(db.String(300), primary_key=True)
    name = db.Column(db.String(300), nullable=True)
    # img = db.Column(db.Text, unique=True, nullable=False)
    mimetype = db.Column(db.String(300), nullable=True)