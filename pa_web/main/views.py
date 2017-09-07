# imports
from datetime import datetime
from flask import request, render_template, render_template, url_for, redirect, flash, current_app
from . import main
from .forms import ContactsForm
from .. import db
from flask_login import login_required

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
