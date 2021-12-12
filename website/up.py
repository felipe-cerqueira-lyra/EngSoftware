from flask import Blueprint, current_app, render_template, request
from website.database.db import db
from website.database.models import File
from uuid import uuid4, uuid5, NAMESPACE_DNS

bp = Blueprint('up', __name__, url_prefix='/up')
static_link = 'http://127.0.0.1:5000/down/'

@bp.route('/', methods=['POST', 'GET'])
def upload_page():
    return render_template("upload.html.jinja")


@bp.route('/register', methods=['POST'])
def register_file():
    file = request.files["file"]
    id_ = str(uuid5(NAMESPACE_DNS, str(uuid4()) + file.filename))
    name_ = file.filename
    mime_type_ = file.mimetype
    link_ = static_link + id_
    file_ = File(id=id_, name=name_, mimetype=mime_type_, link=link_)
    file.save(current_app.config["UPLOAD_FOLDER"] + name_)
    db.session.add(file_)
    db.session.commit()
    type = file_.mimetype.split('/')[0]
    return render_template("download.html.jinja", archive_type=type, file=file_)


@bp.route('/display', methods=['GET'])
def display():
    f = request.files['myFile']
    filename = secure_filename(f.filename)

    f.save(app.config['UPLOAD_FOLDER'] + filename)

    file = open(app.config['UPLOAD_FOLDER'] + filename, "r")
    content = file.read()
