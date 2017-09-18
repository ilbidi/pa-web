# Blueprint for main
from flask import Blueprint

main = Blueprint('main', __name__, template_folder='templates', static_folder='static')

from . import views, errors
from ..models import Permission

# Make the permission class accessible from templates
@main.app_context_processor
def inject_permission():
    return dict(Permission=Permission)
