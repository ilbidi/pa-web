# Forms definition
from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email

class EmailPasswordForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log in')

# Class contacts, send and email
class ContactsForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
    request = TextAreaField('Request')
    submit = SubmitField('Contact us.')
