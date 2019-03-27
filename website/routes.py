from website import application
from flask import render_template

@application.route('/')
@application.route('/home')
def home():
    return render_template('index.html', title="Welcome!")