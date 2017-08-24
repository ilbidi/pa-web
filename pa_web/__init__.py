# Main
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

# Load configurations
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

# Import views, the import is at the end to avoid circular import
from pa_web import views

# Database
db = SQLAlchemy(app)

# Init bootstrap
bootstrap = Bootstrap(app)
