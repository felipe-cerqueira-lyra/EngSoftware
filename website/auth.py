from flask import Blueprint, render_template


bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/logout')
def logout():
    return "<p>Logout<\p>"


@bp.route('/signup')
def signup_page():
    return render_template("signup.html.jinja")


@bp.route('/signin')
def signin_page():
    return render_template("signin.html.jinja")