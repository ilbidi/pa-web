import unittest
from pa_web.models import User, Role, Garden, Plant
from flask import current_app
from pa_web import create_app, db


class PlantModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_plant_crud(self):
        user = User( email='test@test.com', username = 'test', password='test')
        garden = Garden(name = 'test', owner = user)
        plant = Plant(name='test', owner=user, garden = garden)
        db.session.add(plant)
        last_plant = Plant.query.order_by(Plant.id.desc()).first()
        self.assertTrue(last_plant.name == 'test')
        last_plant.name='test_chg'
        db.session.add(last_plant)
        last_plant1 = Plant.query.order_by(Plant.id.desc()).first()
        self.assertTrue(last_plant1.name == 'test_chg')
        db.session.delete(last_plant1)
        plant = Plant(name = 'test_new', owner = user, garden = garden)
        db.session.add(plant)
        self.assertTrue(Plant.query.filter((Plant.name=='test') | (Plant.name=='test_chg')).count() == 0 )
        self.assertTrue(Plant.query.filter(Plant.name=='test_new').count() > 0 )
