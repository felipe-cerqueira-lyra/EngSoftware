import os
from flask import Flask, render_template

from website.database.db import db_init, DB_NAME


def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI=f'sqlite:///{DB_NAME}',
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        UPLOAD_FOLDER=app.root_path + '/database/static/'
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    try:
        os.makedirs(app.instance_path)
    except OSError as e:
        pass

    from website.database import db
    app.register_blueprint(db.bp)
    db_init(app)

    from . import down
    app.register_blueprint(down.bp)
    from . import up
    app.register_blueprint(up.bp)

    @app.route('/')
    def upload():
        return render_template("upload.html.jinja")

    return app
