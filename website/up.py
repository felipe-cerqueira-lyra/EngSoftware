from flask import Blueprint, current_app, render_template, request, flash
from flask_login import current_user

from website.database.db import db
from website.database.models import File, PublicFile
from uuid import uuid4, uuid5, NAMESPACE_DNS

bp = Blueprint('up', __name__, url_prefix='/up')
static_link = 'https://127.0.0.1:5000/down/'


@bp.route('/', methods=['POST', 'GET'])
def upload_page():
    return render_template("upload.html", user=current_user)


@bp.route('/register', methods=['POST'])
def register_file():
    file = request.files["file"]
    id_ = str(uuid5(NAMESPACE_DNS, str(uuid4()) + file.filename))
    name_ = file.filename
    mime_type_ = file.mimetype
    link_ = static_link + id_
    if current_user.is_authenticated:
        file_ = File(id=id_, name=name_, mimetype=mime_type_, link=link_, user_id=current_user.id, numberofdownloads=0)
    else:
        file_ = PublicFile(id=id_, name=name_, mimetype=mime_type_, link=link_, numberofdownloads=0)
    file.save(current_app.config["UPLOAD_FOLDER"] + name_)
    db.session.add(file_)
    db.session.commit()
    type = file_.mimetype.split('/')[0]
    flash('File anchored adequately; you can download or share it below.', category='sucess')
    return render_template("download.html", archive_type=type, file=file_, user=current_user)
