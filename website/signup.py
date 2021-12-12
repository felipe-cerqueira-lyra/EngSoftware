import os

from flask import Blueprint, current_app, render_template, request, send_from_directory

from website.database.models import File

bp = Blueprint('signup', __name__, url_prefix='/signup')


@bp.route('/signup')
def signup_page():
    return render_template("signup.html.jinja")
