import os

from flask import Blueprint, current_app, render_template, request, send_from_directory

from website.database.models import File

bp = Blueprint('signin', __name__, url_prefix='/signin')


@bp.route('/signin')
def signin_page():
    return 'Hello World from Down!'
