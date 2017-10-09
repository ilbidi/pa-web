# Blueprint for Garden
from flask import Blueprint

blog = Blueprint('blog', __name__, template_folder='templates', static_folder='static')

from . import views, errors
