from urllib.request import urlopen
from flask import Blueprint, render_template, request, redirect, url_for, g

from website.database.db import db
from website.database.models import Img

bp = Blueprint('up', __name__, url_prefix='/up')

@bp.route('/', methods=['POST', 'GET'])
def upload_page():
    return(render_template("upload.html.jinja"))

@bp.route('/register', methods=['POST'])
def register_file():
    file = request.files["file"]
    file.save(file.filename)
    return redirect(url_for('up.upload_page'))

@bp.route('/display', methods=['GET'])
def display():
    f = request.files['myFile']
    filename = secure_filename(f.filename)

    f.save(app.config['UPLOAD_FOLDER'] + filename)

    file = open(app.config['UPLOAD_FOLDER'] + filename,"r")
    content = file.read()
