from os import path
from flask import Flask

from website.database.db import db

DB_NAME = "database/database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'C88BA7BB9E343A7BA582E90DCBD1B958A210059069AD58C7B29EF1763BAC2634'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    create_database(app)
    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
