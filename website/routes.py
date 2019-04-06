from website import application
from flask import render_template, redirect, request, flash
from website.forms import LoginForm
from flask_login import current_user, login_user, login_required, logout_user
from website.models import User
from werkzeug.urls import url_parse


@application.route('/')
@application.route('/home')
def home():
    return render_template('index.html', title="Welcome!")

@application.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('account'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title="Log In", form=form)

@application.route('/register')
def register():
    return render_template('register.html', title="Register!")

@application.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@application.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    return render_template('account.html', title="Account")