# imports
from datetime import datetime
from flask import request, render_template, render_template, url_for, redirect, flash, current_app
from . import blog
from .forms import PostInsertForm
from .. import db
from flask_login import login_required, current_user
from ..models import User, Post, Permission
from ..decorators import admin_required 
from pa_web.utils import pa_gis

# User Posts List and post insert
@blog.route('/my-posts', methods =['GET', 'POST'])
@login_required
def my_posts():
   form = PostInsertForm()
   if( current_user.can(Permission.WRITE_POST) and \
       form.validate_on_submit()):
       post = Post( body=form.body.data, author=current_user._get_current_object())
       db.session.add(post)
       db.session.commit()
       return redirect(url_for('blog.my_posts'))
   posts = Post.query.filter_by(author = current_user).order_by(Post.timestamp.desc()).all()
   return render_template('my-posts.html', form=form, posts=posts)
