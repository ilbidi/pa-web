# imports
from datetime import datetime
from flask import request, render_template, render_template, url_for, redirect, flash, current_app
from . import garden
from .forms import GardenInsertForm
from .. import db
from flask_login import login_required, current_user
from ..models import User, Role, Garden
from ..decorators import admin_required 
from pa_web.utils import pa_gis

# Gardens List
@garden.route('/gardens')
@login_required
def list_gardens():
    gardens = Garden.query.filter_by(owner = current_user) 
    return render_template('gardens.html', gardens=gardens)

# Add a new garden
@garden.route('/add-garden', methods=['GET', 'POST'])
@login_required
def add_garden():
    form = GardenInsertForm()
    if(form.validate_on_submit()):
        garden = Garden(name = form.name.data, location=form.location.data, owner=current_user)
        db.session.add(garden)
        db.session.commit()
        return redirect(url_for('garden.list_gardens'))
    return render_template('insert_garden.html', form = form)

# Garden page
@garden.route('/garden/<int:id>')
@login_required
def show_garden(id):
    garden = Garden.query.filter_by( id=garden_id).first()
    if(garden is None):
        abort(404)
    return render_template('garden.html', garden=garden)

# Garden edit page
@garden.route('/edit-garden/<int:id>')
@login_required
def edit_garden(id):
    garden = Garden.query.filter_by( id=garden_id).first()
    if(garden is None):
        abort(404)
    return render_template('garden.html', garden=garden)
