import unittest
from pa_web.models import User, Role, Garden, GardenType
from flask import current_app
from pa_web import create_app, db


class GardenModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_garden_crud(self):
        user = User( email='test@test.com', username = 'test', password='test')
        garden = Garden(name = 'test', owner = user)
        db.session.add(garden)
        last_garden = Garden.query.order_by(Garden.id.desc()).first()
        self.assertTrue(last_garden.name == 'test')
        last_garden.name='test_chg'
        db.session.add(last_garden)
        last_garden1 = Garden.query.order_by(Garden.id.desc()).first()
        self.assertTrue(last_garden1.name == 'test_chg')
        db.session.delete(last_garden1)
        garden = Garden(name = 'test_new', owner = user, garden_type =GardenType.TERRACE)
        db.session.add(garden)
        self.assertTrue(Garden.query.filter((Garden.name=='test') | (Garden.name=='test_chg')).count() == 0 )
        self.assertTrue(Garden.query.filter(Garden.name=='test_new').count() > 0 )
