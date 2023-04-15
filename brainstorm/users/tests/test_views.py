from http import HTTPStatus

from django.db.utils import IntegrityError
from django.shortcuts import reverse
from django.test import Client, TestCase, override_settings
from django.utils import timezone
from unittest.mock import patch

from users.models import User


class SignUpTests(TestCase):
    def setUp(self) -> None:
        self.url = reverse('users:signup')
        self.test_user_data = {
            'username': 'testuser',
            'email': 'test@user.com',
            'password1': 'fF5bo0zTVN',
            'password2': 'fF5bo0zTVN',
        }

    @override_settings(USERS_AUTOACTIVATE=True)
    def test_signup_with_debug_true(self):
        response = Client().post(self.url, data=self.test_user_data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        user = User.objects.get(
            username=self.test_user_data.get('username')
        )
        self.assertTrue(user.is_active)

    @override_settings(USERS_AUTOACTIVATE=False)
    def test_signup_with_debug_false(self):
        response = Client().post(self.url, data=self.test_user_data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        user = User.objects.get(
            username=self.test_user_data.get('username')
        )
        self.assertFalse(user.is_active)

    @override_settings(USERS_AUTOACTIVATE=False)
    def test_activate_user_within_12_hours(self):
        Client().post(self.url, data=self.test_user_data)
        activation_url = reverse(
            'users:activate', args=[self.test_user_data['username']]
        )
        activation_response = Client().get(activation_url)
        self.assertEqual(activation_response.status_code, HTTPStatus.OK)
        user = User.objects.get(
            username=self.test_user_data['username']
        )
        self.assertTrue(user.is_active)

    @override_settings(USERS_AUTOACTIVATE=False)
    def test_activate_user_after_12_hours(self):
        Client().post(self.url, data=self.test_user_data)
        activation_url = reverse(
            'users:activate', args=[self.test_user_data['username']]
        )
        with patch.object(
            timezone,
            'now',
            return_value=timezone.now() + timezone.timedelta(hours=13),
        ):
            activation_response = Client().get(activation_url)
            self.assertEqual(
                activation_response.status_code, HTTPStatus.NOT_FOUND
            )
            user = User.objects.get(
                username=self.test_user_data['username']
            )
            self.assertFalse(user.is_active)

    @override_settings(USERS_AUTOACTIVATE=True)
    def test_yandex_email_formatting(self):
        Client().post(
            self.url,
            {
                'username': 'test',
                'email': 'yandex.test@ya.ru',
                'password1': 'fF5bo0zTVN',
                'password2': 'fF5bo0zTVN',
            },
        )
        user = User.objects.get(username='test')
        self.assertEqual(user.normalized_email, 'yandex-test@yandex.ru')

    @override_settings(USERS_AUTOACTIVATE=True)
    def test_google_email_formatting(self):
        Client().post(
            self.url,
            {
                'username': 'test',
                'email': 'google.test+test@gmail.com',
                'password1': 'fF5bo0zTVN',
                'password2': 'fF5bo0zTVN',
            },
        )
        user = User.objects.get(username='test')
        self.assertEqual(user.normalized_email, 'googletest@gmail.com')

    @override_settings(USERS_AUTOACTIVATE=True)
    def test_with_similar_emails(self):
        Client().post(
            self.url,
            {
                'username': 'test1',
                'email': 'yandex.test@ya.ru',
                'password1': 'fF5bo0zTVN',
                'password2': 'fF5bo0zTVN',
            },
        )
        with self.assertRaises(IntegrityError):
            Client().post(
                self.url,
                {
                    'username': 'test2',
                    'email': 'yandex-test@yandex.ru',
                    'password1': 'fF5bo0zTVN',
                    'password2': 'fF5bo0zTVN',
                },
            )
