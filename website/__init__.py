from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

application = Flask(__name__)
application.config.from_pyfile('config.py')
application.config['SECRET_KEY']
application.config['SQLALCHEMY_DATABASE_URI']
db = SQLAlchemy(application)
migrate = Migrate(application, db)

from website import routes, models