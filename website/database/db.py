from os import path, mkdir

from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint

DB_NAME = "database/database.db"
UP_FOLDER = "database/static"
db = SQLAlchemy()

bp = Blueprint('database', __name__, static_folder='static', url_prefix='/database')

def db_init(app):
    db.init_app(app)
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)

    if not path.exists('website/' + UP_FOLDER):
        mkdir('website/' + UP_FOLDER)

    with app.app_context():
        db.create_all()
    return db
