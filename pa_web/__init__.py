# Main
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Load configurations
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

# Import views, the import is at the end to avoid circular import
from pa_web import views

# Database
db = SQLAlchemy(app)
