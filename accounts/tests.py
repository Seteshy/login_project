from django.test import TestCase
from django.contrib.auth.models import User

class UserTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(username='teste', password='1234')
        self.assertEqual(user.username, 'teste')
        self.assertTrue(user.check_password('1234'))
