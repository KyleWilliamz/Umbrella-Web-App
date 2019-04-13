from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms_components import TimeField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Regexp
from website.models import User
import pycountry

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Log In!')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class LocationForm(FlaskForm):
    codes = [(country.alpha_2, country.name) for country in pycountry.countries]
    cityName = StringField('City', validators=[DataRequired()])
    country = SelectField( 'Country', choices=codes, validators=[DataRequired()])
    time = TimeField('Notification Time', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired(), Regexp('^\D?(\d{3})\D?\D?(\d{3})\D?(\d{4})$', flags=0, message='Please enter a valid US Phone Number with the area code.')]) 
    submit = SubmitField('Add')
