# Forms definition
from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Required, Email, Length, Regexp, EqualTo
from wtforms import ValidationError

from ..models import User


class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(1,128)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Log in')

# User Registration Form
class UserRegistrationForm(Form):
    """A user must provide a unique email and name and a password"""
    email = StringField('Email', validators=[Required(), Email(), Length(1,128)])
    username = StringField('User name', validators=[Required(), Length(1,128), \
                                                    Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, \
                                                           'Usernames must have only letters, ' \
                                                           'numbers, dots or underscores')
                                                    ])
    password = PasswordField('Password', validators=[Required(), \
                                                     Length(1,128), \
                                                     EqualTo('password2', message='Passwords does not match.') \
                                                     ])
    password2 = PasswordField('Reenter Password', validators=[Required(), \
                                                      Length(1,128)
                                                      ])
    submit = SubmitField('Register')

# Validators
# If a form define a mathod wich name begins with validate_ this method is automatically invoked
# at the field indated in method name
def validate_email(self, field):
    if(User.query.filter_by(email=field.data).first() ):
        raise ValidationError('Email already registered.')

def validate_username(self, field):
    if( User.query.filter_by(username=field.data).first() ):
        raise ValidationError('Username already exist, please chose a different one.')
