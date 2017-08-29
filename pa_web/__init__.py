# Main
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from config import config

# Database
db = SQLAlchemy()

# Init bootstrap
bootstrap = Bootstrap()

# Init email
mail = Mail()

# Init Moment
moment = Moment()

# App creation
def create_app(config_name):
    """Creation of the app"""
    app = Flask(__name__)
    app.config.from_object(config[config_name ])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    # Blueprints
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
