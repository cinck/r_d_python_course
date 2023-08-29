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


class TestUserViews(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(username='test_user', password='test_password', age='18')

    def test_users_list_view(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/users_list.html')
        self.assertContains(response, 'test_user')

    def test_users_detail_view(self):
        response = self.client.get(f'/users/{self.user.pk}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/users_detail.html')
        self.assertContains(response, 'test_user')

    def test_users_create_view(self):
        response = self.client.post(
            f'/users/create/',
            {
                'username': 'test_user_create',
                'password': 'test_password',
                'age': 18
            }
        )
        self.assertEqual(response.status_code, 302)

    def test_users_delete_view(self):
        response = self.client.post(
            f'/users/create/',
            {
                'username': 'test_user_create',
                'password': 'test_password',
                'age': 18
            }
        )
        self.assertEqual(response.status_code, 302)

