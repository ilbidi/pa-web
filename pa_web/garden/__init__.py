# Blueprint for Garden
from flask import Blueprint

garden = Blueprint('garden', __name__, template_folder='templates', static_folder='static')

from . import views, errors
