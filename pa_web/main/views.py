# imports
from datetime import datetime
from flask import request, render_template, render_template, url_for, redirect, flash, current_app
from . import main
from .forms import ContactsForm, EditProfileForm, EditProfileAdminForm
from .. import db
from flask_login import login_required, current_user
from ..models import User, Role
from ..decorators import admin_required
from pa_web.utils import pa_gis

# Emails
from pa_web.emails import send_email

# Index
@main.route('/')
@main.route('/index')
def index():
    return render_template('index.html')

# Contacts
@main.route('/contacts', methods=['GET', 'POST'])
def contacts():
    form = ContactsForm()
    if( form.validate_on_submit() ):
        flash('Thanks for your request %s, we will contact you.'%form.email.data)
        send_email(current_app.config['PAWEB_SUBJECT_PREFIX'] + '- Contact request.',
                   current_app.config['PAWEB_MAIL_SENDER'],
                   form.email.data,
                   form.request.data,
                   form.request.data)

        return redirect(url_for('.contacts'))
    return render_template('contacts.html', form=form)

# Meteo in arrakis
@main.route('/meteo')
@login_required
def meteo():
    return render_template('meteo.html')

# Profile page
@main.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by( username=username).first()
    if(user is None):
        abort(404)
    return render_template('user.html', user=user, geolocated_location = pa_gis.get_location(user.location))

# Edit User Profile page
@main.route('/edit-profile', methods=['GET', 'POST'] )
@login_required
def edit_profile():
    form = EditProfileForm()
    if( form.validate_on_submit()):
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        db.session.add(current_user)
        flash('Your profile has been updated.')
        return redirect(url_for('.user', username=current_user.username))
    form.name.data = current_user.name
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', form=form)

# Admin Edit User Profile page
@main.route('/edit-profile/<int:id>', methods=['GET', 'POST'] )
@login_required
@admin_required
def edit_profile_admin(id):
    user = User.query.get_or_404(id)
    form = EditProfileAdminForm(user=user)
    if( form.validate_on_submit()):
        user.email = form.email.data
        user.username = form.username.data
        user.confirmed = form.confirmed.data
        user.role = Role.query.get(form.role.data)
        user.name = form.name.data
        user.location = form.location.data
        user.about_me = form.about_me.data
        db.session.add(user)
        flash('User %s profile has been updated.' % user.username )
        return redirect(url_for('.user', username=user.username))
    form.email.data = user.email
    form.username.data = user.username
    form.confirmed.data = user.confirmed
    form.role.data = user.role_id
    form.name.data = user.name
    form.location.data = user.location
    form.about_me.data = user.about_me
    return render_template('edit_profile.html', form=form)
