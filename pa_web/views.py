# imports
from flask import request, render_template, render_template, url_for

# views
from pa_web import app
from pa_web.forms import EmailPasswordForm

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
