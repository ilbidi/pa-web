# Forms definition
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Required, Email, Length, Regexp, EqualTo
from wtforms import ValidationError

from ..models import User, Garden


# Insert a new garden
class GardenInsertForm(FlaskForm):
    """Insert a garden"""
    name = StringField('Garden name', validators=[Required(), Length(1,128), \
                                                    Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, \
                                                           'Garden names must have only letters, ' \
                                                           'numbers, dots or underscores')
                                                    ])
    location = StringField('Location', validators=[Length(0, 128)])
    submit = SubmitField('Add garden')

# User Edit profile form
class GardenEditForm(FlaskForm):
    """Edit a garden"""
    name = StringField('Garden name', validators=[Required(), Length(1,128), \
                                                    Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, \
                                                           'Garden names must have only letters, ' \
                                                           'numbers, dots or underscores')
                                                    ])
    location = StringField('Location', validators=[Length(0, 128)])
    submit = SubmitField('Update garden')
    delete = SubmitField('Delete garden')

