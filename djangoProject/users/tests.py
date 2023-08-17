from django.contrib.auth import get_user_model
from django.test import TestCase


class TestUserModel(TestCase):
    test_data = {
        'username': 'test_name',
        'password': 'test_password',
        'age': '18'
    }

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create(username='test_name', password='test_password', age=18)

    def test_user_creation(self):
        self.assertEqual(self.user.username, self.test_data['username'])
        self.assertEqual(self.user.password, self.test_data['password'])
        self.assertEqual(self.user.age, self.test_data['age'])