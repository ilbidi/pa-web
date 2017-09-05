import unittest
from pa_web.models import User

class UserModelTestCase(unittest.TestCase):
    def test_password_setter(self):
        user = User( username = 'test', password='test1')
        self.assertTrue(user.password_hash is not None)

    def test_no_password_getter(self):
        user = User( username = 'test', password='test1')
        with self.assertRaises(AttributeError):
            user.password
