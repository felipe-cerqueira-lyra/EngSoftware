import json

from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from website.database.models import File

from website.database.db import db

bp = Blueprint('home', __name__)


@bp.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user)


@bp.route('/delete/<id>', methods=['GET', 'POST'])
def delete_file(id):
    file = File.query.filter_by(id=id).first()
    if file:
        if file.user_id == current_user.id:
            db.session.delete(file)
            db.session.commit()
    return render_template("home.html", user=current_user)

