import os
from flask import Flask, render_template


def create_app(test_config=None):
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
    )
    toolbar = DebugToolbarExtension(app)
    app.config['DEBUG_TB_PANELS'] += ('flask_mongoengine.panels.MongoDebugPanel',)
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
    if test_config == None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    try:
        os.makedirs(app.instance_path)
    except OSError as e:
        pass

    # from . import db
    # db.app_init(app)

    from . import down.py
    app.register_blueprint(library.bp)

    @app.route('/')
    def index():
        return render_template('home.html.jinja')

    return app
