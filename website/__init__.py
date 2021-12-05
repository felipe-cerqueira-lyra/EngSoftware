import os
from flask import Flask, render_template

from website.database.db import db_init, DB_NAME



def create_app(test_config=None):
    app = Flask(__name__)
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_mapping(
        # SECRET_KEY = 'C88BA7BB9E343A7BA582E90DCBD1B958A210059069AD58C7B29EF1763BAC2634'
        SECRET_KEY = 'dev',
        SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB_NAME}',
        SQLALCHEMY_TRACK_MODIFICATIONS = False,
        UPLOAD_FOLDER = "database/files"
    )

    if test_config == None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    try:
        os.makedirs(app.instance_path)
    except OSError as e:
        pass

    db_init(app)

    from . import down
    app.register_blueprint(down.bp)
    from . import up
    app.register_blueprint(up.bp)


    @app.route('/')
    def index():
        return ('Hello World')

    return app
