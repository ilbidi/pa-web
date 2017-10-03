# imports
from datetime import datetime
from flask import request, render_template, render_template, url_for, redirect, flash, current_app
from . import garden
from .forms import GardenInsertForm, GardenEditForm
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
@garden.route('/garden/<int:garden_id>')
@login_required
def show_garden(garden_id):
    garden = Garden.query.filter_by( id=garden_id, owner=current_user).first()
    if(garden is None):
        abort(404)
    return render_template('garden.html', garden=garden)

# Garden edit page
@garden.route('/edit-garden/<int:garden_id>', methods=['GET', 'POST'])
@login_required
def edit_garden(garden_id):
    form = GardenEditForm()
    garden = Garden.query.filter_by( id=garden_id, owner=current_user).first()
    if(garden is None):
        abort(404)
    if( form.validate_on_submit()):
        if( form.submit.data ):
            # Pressed submit data
            garden.name = form.name.data
            garden.location = form.location.data
            db.session.add(garden)
            return redirect(url_for('garden.show_garden', garden_id=garden.id))
        elif( form.delete.data ):
            # Pressed delete
            db.session.delete(garden)
            return redirect(url_for('garden.list_gardens'))
    form.name.data = garden.name
    form.location.data = garden.location
    return render_template('edit_garden.html', form=form)
