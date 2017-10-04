# Forms definition
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Required, Email, Length, Regexp, EqualTo
from wtforms import ValidationError

from ..models import User, Garden, Plant


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

# Garden Edit form
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


# Insert a new plant
class PlantInsertForm(FlaskForm):
    """Insert a plant"""
    name = StringField('Plant name', validators=[Required(), Length(1,128), \
                                                    Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, \
                                                           'Plant names must have only letters, ' \
                                                           'numbers, dots or underscores')
                                                    ])
    description = StringField('Plant description', validators=[ Length(0,1024)])
    # TODO Garden
    submit = SubmitField('Add plant')

# Plant Edit profile form
class PlantEditForm(FlaskForm):
    """Edit a plant"""
    name = StringField('Plant name', validators=[Required(), Length(1,128), \
                                                    Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, \
                                                           'Plant names must have only letters, ' \
                                                           'numbers, dots or underscores')
                                                    ])
    description = StringField('Plant description', validators=[ Length(0,1024)])
    # TODO Garden
    submit = SubmitField('Update plant')
    delete = SubmitField('Delete plant')

