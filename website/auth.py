from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from website.database.db import db

from website.database.models import User

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.signin_page'))


@bp.route('/signup', methods=['GET', 'POST'])
def signup_page():
    if request.method == 'POST':
        name = request.form.get('name')
        surname = request.form.get('surname')
        user = request.form.get('user')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user_check = User.query.filter_by(email=email).first()
        if user_check:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 1:
            flash('Password must be at least 1 characters.', category='error')
        else:
            new_user = User(
                email=email,
                name=name,
                surname=surname,
                user=user,
                password=generate_password_hash(password1, method='sha256')
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            return redirect(url_for('home.home'))
        return render_template("signup.html")
    flash('Create a new user below.', category='sucess')
    return render_template("signup.html", user=current_user)


@bp.route('/signin', methods=['GET', 'POST'])
def signin_page():
    if request.method == 'POST':
        user = request.form.get('user')
        password = request.form.get('password')
        user_check = User.query.filter_by(user=user).first()
        if user_check:
            if check_password_hash(user_check.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user_check, remember=True)
                return redirect(url_for('home.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('User does not exist.', category='error')
    flash('Login user below.', category='sucess')
    return render_template("signin.html", user=current_user)
