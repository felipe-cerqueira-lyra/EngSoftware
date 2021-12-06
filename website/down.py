from urllib.request import urlopen
from flask import Blueprint, current_app, render_template, request, redirect, url_for, send_from_directory, send_file, g

from website.database.db import db, Img
import os
# from website.database.models import Img

bp = Blueprint('down', __name__, url_prefix='/down')

@bp.route('/', methods=['POST', 'GET'])
def download_page():
    return ('Hello World from Down!')



@bp.route('/<id>', methods=['POST', 'GET'])
def download_file(id):
    if request.method == 'GET':
        file = Img.query.filter_by(id=id).first()
        if not file:
            return 'No img with that id', 404
        type = file.mimetype.split('/')[0]
        return (render_template("download.html.jinja",archive_type=type,file=file))
    if request.method == 'POST':
        file = Img.query.filter_by(id=id).first()
        if not file:
            return 'No img with id %s'%id
        return send_from_directory(current_app.config["UPLOAD_FOLDER"], filename=file.name , as_attachment=True)
