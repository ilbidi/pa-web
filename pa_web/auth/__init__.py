# Blueprint for main
from flask import Blueprint

main = Blueprint('auth', __name__, template_folder='templates', static_folder='static')

from . import views, errors
