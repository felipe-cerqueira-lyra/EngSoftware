from urllib.request import urlopen
from flask import Blueprint, render_template, request, redirect, url_for, g

from website.database.db import db, Img
# from website.database.models import Img

bp = Blueprint('down', __name__, url_prefix='/down')

@bp.route('/', methods=['POST', 'GET'])
def download_page():
    return("Hello World from Down!")



@bp.route('/<id>', methods=['POST', 'GET'])
def download_file(id):
    if request.method == 'GET':
        img = Img.query.filter_by(id=id).first()
        if not img:
            return 'No img with that id', 404
        return (img.name)
