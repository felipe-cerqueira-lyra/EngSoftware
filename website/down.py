from urllib.request import urlopen
from flask import Blueprint, current_app, render_template, request, redirect, url_for, send_from_directory, send_file, g

from website.database.db import db, Img
import os
# from website.database.models import Img

bp = Blueprint('down', __name__, url_prefix='/down')

@bp.route('/', methods=['POST', 'GET'])
def download_page():
    return (render_template("download.html.jinja"))



@bp.route('/<id>', methods=['POST', 'GET'])
def download_file(id):
    if request.method == 'GET':
        img = Img.query.filter_by(id=id).first()
        if not img:
            return 'No img with that id', 404
        return (render_template("download.html.jinja",archive_type="img",file=img))
    if request.method == 'POST':
        file = Img.query.filter_by(id=id).first()
        print(file.name, file.id)
        print(url_for('database.static', filename=file.name))
        if not file:
            return 'No img with id %s'%id
        return send_from_directory(current_app.config["UPLOAD_FOLDER"], filename=file.name , as_attachment=True)
