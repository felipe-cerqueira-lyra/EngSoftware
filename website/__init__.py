from os import path
from flask import Flask

from website.database.db import db_init, DB_NAME


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'C88BA7BB9E343A7BA582E90DCBD1B958A210059069AD58C7B29EF1763BAC2634'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db_init(app)

    return app
