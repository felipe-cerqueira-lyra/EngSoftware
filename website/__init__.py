import os
from flask import Flask, render_template
from flask_login import LoginManager

from website.database.db import db_init, DB_NAME
from website.database.models import User


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
    db = db_init(app)

    from . import down
    app.register_blueprint(down.bp)
    from . import up
    app.register_blueprint(up.bp)
    from . import auth
    app.register_blueprint(auth.bp)
    from . import home
    app.register_blueprint(home.bp)

    @app.before_first_request
    def create_tables():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'home.home'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
