from website import application
from flask import render_template
from website.forms import LoginForm

@application.route('/')
@application.route('/home')
def home():
    return render_template('index.html', title="Welcome!")

@application.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title="Log In", form=form)