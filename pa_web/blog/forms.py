# Forms definition
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, BooleanField, SelectField
from wtforms.validators import DataRequired, Required, Email, Length, Regexp, EqualTo
from wtforms import ValidationError

# Insert a new post
class PostInsertForm(FlaskForm):
    """Insert a post"""
    body = TextAreaField('Any ideas?', validators=[Required()])
    submit = SubmitField('Submit')

