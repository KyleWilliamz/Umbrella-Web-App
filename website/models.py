from website import db, LoginManager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from website import login


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    locations = db.relationship('Locations', backref='author', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Locations(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    cityName = db.Column(db.String(64), nullable=False)
    country = db.Column(db.String(64), nullable=False)
    time = db.Column(db.Integer)
    phone = db.Column(db.String(32), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


    def __repr__(self):
        return f"Location('{self.cityName}', '{self.country}', '{self.time}', {self.phone})"