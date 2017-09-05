# Forms definition
from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(1,128)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Log in')
