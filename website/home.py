from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from website.database.models import File

bp = Blueprint('home', __name__)


@bp.route('/', methods=['GET', 'POST'])
@login_required
def home():
    id = "36aff26a-2d2b-5cdc-92f2-cd8d78fdbf46" 
    files_ = File.query.filter_by(id=id).first()
    file_ = [{"_id" : 1, "file" : files_}, {"_id" : 2, "file" : files_}, {"_id" : 3, "file" : files_}, {"_id" : 4, "file" : files_}]
    if not file_:
            return 'No img with that id', 404
    return render_template("home.html", user=current_user, files=file_)