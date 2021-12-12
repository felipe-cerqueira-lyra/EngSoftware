import os

from flask import Blueprint, current_app, render_template, request, send_from_directory

from website.database.models import File

bp = Blueprint('down', __name__, url_prefix='/down')


@bp.route('/', methods=['POST', 'GET'])
def download_page():
    return 'Hello World from Down!'


@bp.route('/<id>', methods=['POST', 'GET'])
def download_file(id):
    if request.method == 'GET':
        file_ = File.query.filter_by(id=id).first()
        if not file_:
            return 'No img with that id', 404
        type = file_.mimetype.split('/')[0]
        return render_template("download.html.jinja", archive_type=type, file=file_)
    if request.method == 'POST':
        file_ = File.query.filter_by(id=id).first()
        if not file_:
            return 'No img with id %s' % id
        uploads = os.path.join(current_app.root_path, current_app.config['UPLOAD_FOLDER'])
        return send_from_directory(directory=uploads, path=current_app.static_folder, filename=file_.name, as_attachment=True)
