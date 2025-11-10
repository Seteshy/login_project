from django.test import TestCase
from django.contrib.auth.models import User

class UserTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(username='teste', password='123')
        self.assertEqual(user.username, 'teste')
