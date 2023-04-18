import http
import unittest.mock

import django.db.utils
import django.shortcuts
import django.test
import django.utils

import users.models


class SignUpTests(django.test.TestCase):
    def setUp(self) -> None:
        self.url = django.shortcuts.reverse('users:signup')
        self.test_user_data = {
            'username': 'testuser',
            'email': 'test@user.com',
            'password1': 'fF5bo0zTVN',
            'password2': 'fF5bo0zTVN',
        }

    @django.test.override_settings(USERS_AUTOACTIVATE=True)
    def test_signup_with_debug_true(self):
        response = django.test.Client().post(
            self.url, data=self.test_user_data
        )
        self.assertEqual(response.status_code, http.HTTPStatus.FOUND)
        user = users.models.User.objects.get(
            username=self.test_user_data.get('username')
        )
        self.assertTrue(user.is_active)

    @django.test.override_settings(USERS_AUTOACTIVATE=False)
    def test_signup_with_debug_false(self):
        response = django.test.Client().post(
            self.url, data=self.test_user_data
        )
        self.assertEqual(response.status_code, http.HTTPStatus.FOUND)
        user = users.models.User.objects.get(
            username=self.test_user_data.get('username')
        )
        self.assertFalse(user.is_active)

    @django.test.override_settings(USERS_AUTOACTIVATE=False)
    def test_activate_user_within_12_hours(self):
        django.test.Client().post(self.url, data=self.test_user_data)
        activation_url = django.shortcuts.reverse(
            'users:activate', args=[self.test_user_data['username']]
        )
        activation_response = django.test.Client().get(activation_url)
        self.assertEqual(activation_response.status_code, http.HTTPStatus.OK)
        user = users.models.User.objects.get(
            username=self.test_user_data['username']
        )
        self.assertTrue(user.is_active)

    @django.test.override_settings(USERS_AUTOACTIVATE=False)
    def test_activate_user_after_12_hours(self):
        django.test.Client().post(self.url, data=self.test_user_data)
        activation_url = django.shortcuts.reverse(
            'users:activate', args=[self.test_user_data['username']]
        )
        with unittest.mock.patch.object(
            django.utils.timezone,
            'now',
            return_value=(
                django.utils.timezone.now()
                + django.utils.timezone.timedelta(hours=13)
            ),
        ):
            activation_response = django.test.Client().get(activation_url)
            self.assertEqual(
                activation_response.status_code, http.HTTPStatus.NOT_FOUND
            )
            user = users.models.User.objects.get(
                username=self.test_user_data['username']
            )
            self.assertFalse(user.is_active)

    @django.test.override_settings(USERS_AUTOACTIVATE=True)
    def test_yandex_email_formatting(self):
        django.test.Client().post(
            self.url,
            {
                'username': 'test',
                'email': 'yandex.test@ya.ru',
                'password1': 'fF5bo0zTVN',
                'password2': 'fF5bo0zTVN',
            },
        )
        user = users.models.User.objects.get(username='test')
        self.assertEqual(user.normalized_email, 'yandex-test@yandex.ru')

    @django.test.override_settings(USERS_AUTOACTIVATE=True)
    def test_google_email_formatting(self):
        django.test.Client().post(
            self.url,
            {
                'username': 'test',
                'email': 'google.test+test@gmail.com',
                'password1': 'fF5bo0zTVN',
                'password2': 'fF5bo0zTVN',
            },
        )
        user = users.models.User.objects.get(username='test')
        self.assertEqual(user.normalized_email, 'googletest@gmail.com')

    @django.test.override_settings(USERS_AUTOACTIVATE=True)
    def test_with_similar_emails(self):
        django.test.Client().post(
            self.url,
            {
                'username': 'test1',
                'email': 'yandex.test@ya.ru',
                'password1': 'fF5bo0zTVN',
                'password2': 'fF5bo0zTVN',
            },
        )
        with self.assertRaises(django.db.utils.IntegrityError):
            django.test.Client().post(
                self.url,
                {
                    'username': 'test2',
                    'email': 'yandex-test@yandex.ru',
                    'password1': 'fF5bo0zTVN',
                    'password2': 'fF5bo0zTVN',
                },
            )
