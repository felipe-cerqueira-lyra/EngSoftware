from flask import Blueprint, render_template, request
from website.database.db import db

from website.database.models import User

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/logout')
def logout():
    return "<p>Logout<\p>"


@bp.route('/signup', methods=['GET', 'POST'])
def signup_page():
    if request.method == 'POST':
        first_name = request.form.get('name')
        last_name = request.form.get('last_name')
        user = request.form.get('user')
        email = request.form.get('mail')
        password = request.form.get('pass')
        conf_passw = request.form.get('confirm_password')
        #TODO (Thales): Implement fields validation
        new_user = User(first_name=first_name, last_name=last_name, user=user, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

    return render_template("signup.html")


@bp.route('/signin', methods=['GET', 'POST'])
def signin_page():
    return render_template("signin.html")