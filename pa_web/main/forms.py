# Forms definition
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, BooleanField, SelectField
from wtforms.validators import DataRequired, Email, Length, Required, Regexp, ValidationError

from ..models import User, Role

# Class contacts, send and email
class ContactsForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    request = TextAreaField('Request')
    submit = SubmitField('Contact us.')

# User Edit profile form
class EditProfileForm(FlaskForm):
    name = StringField('Real name', validators=[Length(0, 128)])
    location = StringField('Location', validators=[Length(0, 128)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')
    
# User Edit profile admin form
class EditProfileAdminForm(FlaskForm):
    email = StringField('Email', validators=[Required(), Email(), Length(1,128)])
    username = StringField('User name', validators=[Required(), Length(1,128), \
                                                    Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, \
                                                           'Usernames must have only letters, ' \
                                                           'numbers, dots or underscores')
                                                    ])
    confirmed = BooleanField('Confirmed')
    role = SelectField('Role', coerce=int)
    name = StringField('Real name', validators=[Length(0, 128)])
    location = StringField('Location', validators=[Length(0, 128)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [ (role.id, role.name) \
                              for role in Role.query.order_by(Role.name).all() ]
        self.user = user
                       
    # Validators
    # If a form define a method wich name begins with validate_ this method is automatically invoked
    # at the field indated in method name
    def validate_email(self, field):
        if(field.data != self.user.email and User.query.filter_by(email=field.data).first() ):
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if( field.data != self.user.username and User.query.filter_by(username=field.data).first() ):
            raise ValidationError('Username already exist, please chose a different one.')

