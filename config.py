import os
# Base dir is the dir where this file config.py is located
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hardtoguesssecretKEY'
    PAWEB_SUBJECT_PREFIX='[Project Arrakis]'
    PAWEB_MAIL_SENDER='fbidinotto@gmail.com'
    PAWEB_ADMIN = os.environ.get('PAWEB_ADMIN')
    BCRYPT_LEVEL=12 # Bcrypt config parameter

    @staticmethod
    def init_app(app):
        pass
    
class DevelopementConfig(Config):
    DEBUG = True
    # Email Configuration
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USE_SSL=False
    MAIL_USERNAME='fbidinotto@gmail.com'
    MAIL_PASSWORD='Fbidin88++'
    # SqlAlchemy config
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    # Local file db
    SQLALCHEMY_DATABASE_URI= os.environ.get('DEV_DATABASE_URL') or \
                             'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
    TESTING = True
    # Email Configuration
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USE_SSL=False
    MAIL_USERNAME='fbidinotto@gmail.com'
    MAIL_PASSWORD='Fbidin88++'
    # SqlAlchemy config
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    # Local file db
    SQLALCHEMY_DATABASE_URI= os.environ.get('TEST_DATABASE_URL') or \
                             'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    # Local file db
    SQLALCHEMY_DATABASE_URI= os.environ.get('DATABASE_URL') or \
                             'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
    'developement': DevelopementConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopementConfig
    }
