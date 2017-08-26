# imports
from flask import request, render_template, render_template, url_for, redirect, flash

# views
from pa_web import app
from pa_web.forms import EmailPasswordForm, ContactsForm

# Emails
from .emails import send_email

# Index
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# About
@app.route('/about')
def about():
    return 'About'

# Passing parameters
@app.route('/param/<param>')
def param(param):
    return param

# Enviroment informations
@app.route('/envinfo')
def envinfo():
    user_agent = request.headers.get('User-Agent')
    return '<p>User Agent = %s</p>' % user_agent

# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = EmailPasswordForm()
    if( form.validate_on_submit() ):
        return redirect(url_for('index'))
    return render_template('login.html', form=form)

# Managing redirect errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Contacts
@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
    form = ContactsForm()
    if( form.validate_on_submit() ):
        flash('Thanks for your request %s, we will contact you.'%form.email.data)
        send_email(app.config['PAWEB_SUBJECT_PREFIX'] + '- Contact request.',
                   app.config['PAWEB_MAIL_SENDER'],
                   form.email.data,
                   form.request.data,
                   form.request.data) 
            
        return redirect(url_for('contacts'))
    return render_template('contacts.html', form=form)
