import unittest
from pa_web.models import User, Role, Permission, AnonymousUser
from flask import current_app
from pa_web import create_app, db


class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_setter(self):
        user = User( username = 'test', password='test1')
        self.assertTrue(user.password_hash is not None)

    def test_no_password_getter(self):
        user = User( username = 'test', password='test1')
        with self.assertRaises(AttributeError):
            user.password

    def test_roles_and_permissin(self):
        Role.insert_roles()
        u = User(email = 'test@test.com', password='test')
        self.assertTrue(u.can(Permission.FOLLOW))
        self.assertTrue(u.can(Permission.COMMENT))
        self.assertTrue(u.can(Permission.WRITE_POST))
        self.assertFalse(u.can(Permission.ADMINISTRATOR))

    def testAnonymousUser(self):
        u = AnonymousUser()
        self.assertFalse(u.can(Permission.FOLLOW))
        self.assertFalse(u.can(Permission.COMMENT))
        self.assertFalse(u.can(Permission.WRITE_POST))
        self.assertFalse(u.can(Permission.ADMINISTRATOR))
