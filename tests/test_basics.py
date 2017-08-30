# Basic test
import unittest
from flask import current_app
from pa_web import create_app, db
from pa_web.models import Role

class BasicTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_existing(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])

    def test_app_role_insert(self):
        """Inserting and deleting a role"""
        role = Role( name='test_role')
        db.session.add(role)
        db.session.commit()
        num_of_role = Role.query.filter_by(name=role.name).count()
        self.assertTrue(num_of_role==1)
        db.session.delete(role)
        db.session.commit()
        num_of_role = Role.query.filter_by(name=role.name).count()
        self.assertTrue(num_of_role==0)
        
