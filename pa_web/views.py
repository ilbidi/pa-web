# imports
from flask import request, render_template

# views
from pa_web import app

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
