# imports
from datetime import datetime
from flask import request, render_template, render_template, url_for, redirect, flash, current_app
from . import auth
from .. import db
from .forms import LoginForm
from ..models import User
from flask_login import login_user, logout_user, login_required

# Emails
from pa_web.emails import send_email

# Login
@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if( form.validate_on_submit()):
        user = User.query.filter_by( email = form.email.data).first()
        if( user is not None and user.verify_password(form.password.data)):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Login error')
    return render_template('login.html', form = form)

# Logout
@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash('Logged out')
    return redirect(url_for('main.index'))
