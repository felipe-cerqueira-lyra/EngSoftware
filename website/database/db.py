from os import path

from flask_sqlalchemy import SQLAlchemy

DB_NAME = "database/database.db"
db = SQLAlchemy()

class Img(db.Model):
    id = db.Column(db.String(300), primary_key=True)
    name = db.Column(db.String(300), nullable=True)
    # img = db.Column(db.Text, unique=True, nullable=False)
    mimetype = db.Column(db.String(300), nullable=True)


def db_init(app):
    db.init_app(app)
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        db.session.commit()

    with app.app_context():
        db.create_all()
    return db
