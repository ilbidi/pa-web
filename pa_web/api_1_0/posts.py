# Resource handlers for posts
from . import api
from flask import jsonify
from flask_login import login_required
from ..models import Post

# Return all posts
@api.route('/post/')
def get_posts():
    posts = Post.query.all()
    return jsonify({'posts' : [post.to_json() for post in posts]})

# Return a single post
@api.route('/post/<int:id>')
def get_post(id):
    post = Post.query.get_or_404(id)
    return jsonify(post.to_json())
