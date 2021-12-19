from flask import Blueprint

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/login')
def login():
    return "<p>Login<\p>"


@bp.route('/logout')
def logout():
    return "<p>Logout<\p>"


@bp.route('/sign-up')
def sign_up():
    return "<p>Sign Up<\p>"
