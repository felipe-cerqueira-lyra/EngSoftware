from os import path

from flask_sqlalchemy import SQLAlchemy

DB_NAME = "database/database.db"
db = SQLAlchemy()


def db_init(app):
    db.init_app(app)
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)

    with app.app_context():
        db.create_all()
