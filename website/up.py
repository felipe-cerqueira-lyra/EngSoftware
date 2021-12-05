from urllib.request import urlopen
from flask import Blueprint, render_template, request, redirect, url_for, g

from website.database.db import db
from website.database.models import Img

bp = Blueprint('up', __name__, url_prefix='/up')

@bp.route('/', methods=['POST', 'GET'])
def download_page():
    return("Hello World from Up!")



@bp.route('/<id>', methods=['POST', 'GET'])
def upload_file(id):
    if request.method == 'GET':
        img = Img.query.filter_by(id=id).first()
        if not img:
            return 'No img with that id', 404
        return Response(img.img, mimetype=img.mimetype)
