from flask import Blueprint, render_template, request


bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/logout')
def logout():
    return "<p>Logout<\p>"


@bp.route('/signup', methods=['GET', 'POST'])
def signup_page():
    if request.method == 'POST':
        name = request.form.get('name')
        last_name = request.form.get('last_name')
        user = request.form.get('user')
        mail = request.form.get('mail')
        passw = request.form.get('pass')
        conf_passw = request.form.get('confirm_password')

    return render_template("signup.html")


@bp.route('/signin', methods=['GET', 'POST'])
def signin_page():
    return render_template("signin.html")