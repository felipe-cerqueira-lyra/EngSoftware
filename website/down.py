from urllib.request import urlopen
from flask import Blueprint, render_template, request, redirect, url_for, g

bp = Blueprint('down', __name__, url_prefix='/down')

@bp.route('/', methods=['POST', 'GET'])
def download_page():
    return("Hello World")



@bp.route('/<id>', methods=['POST', 'GET'])
def download_file(id):
    if request.method == 'GET':
