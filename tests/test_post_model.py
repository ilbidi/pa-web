import unittest
from pa_web.models import User, Role, Post
from flask import current_app
from pa_web import create_app, db


class PostModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_post_crud(self):
        user = User( email='test@test.com', username = 'test', password='test')
        post = Post(body = 'test', author = user)
        db.session.add(post)
        last_post = Post.query.order_by(Post.timestamp.desc()).first()
        self.assertTrue(last_post.body == 'test')
        last_post.body='test_chg'
        db.session.add(last_post)
        last_post1 = Post.query.order_by(Post.timestamp.desc()).first()
        self.assertTrue(last_post1.body == 'test_chg')
        db.session.delete(last_post1)
        post = Post(body = 'test_new', author = user)
        self.assertTrue(Post.query.filter((Post.body=='test') | (Post.body=='test_chg')).count() == 0 )
        self.assertTrue(Post.query.filter(Post.body=='test_new').count() > 0 )
