# imports
from datetime import datetime
from flask import request, render_template, render_template, url_for, redirect, flash, current_app
from . import auth
from .. import db
from .forms import LoginForm, UserRegistrationForm
from ..models import User
from ..emails import send_email, send_email_template
from flask_login import login_user, logout_user, login_required, current_user

# Emails
from pa_web.emails import send_email

# checking unconfirmed users
@auth.before_app_request
def before_request():
    if( current_user.is_authenticated ):
        current_user.ping()
        if( not current_user.confirmed \
            and request.endpoint[:5] != 'auth.' ):
            return redirect(url_for('auth.unconfirmed'))

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

# Register
@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = UserRegistrationForm()
    if( form.validate_on_submit()):
        user = User(email = form.email.data, username=form.username.data, \
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmation_token()
        send_email_template(form.email.data, \
                            'Confirm your account', \
                            'emails/register_confirm', \
                            user=user, token=token \
                            )
        flash('An email was sent to %s, please confirm your registration.' % form.email.data)
        return redirect(url_for('main.index'))
    return render_template('register.html', form = form)

# confirm
@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if(current_user.confirmed):
        return redirect(url_for('main.index'))
    if(current_user.confirm(token)):
        flash('Your account is confirmed.')
    else:
        flash('The link you provide was invalid or has expired, register again please.')
    return redirect(url_for('main.index'))

# Unconfirmed user
@auth.route('/unconfirmed')
def unconfirmed():
    if( current_user.is_anonymous or \
        current_user.confirmed ):
        return redirect(url_for('main.index'))
    return render_template('unconfirmed.html')

# Resend confirmation email
@auth.route('/confirm')
@login_required
def resend_confirmation():
    token = current_user.generate_confirmation_token()
    send_email_template(form.email.data, \
                        'Confirm your account', \
                        'emails/register_confirm', \
                        user=user, token=token \
    )
    flash('An email was sent to %s, please confirm your registration.' % current_user.email)
    return redirect(url_for('main.index'))
