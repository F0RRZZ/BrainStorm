import random
import string

import django.test
import django.urls
import parameterized

import projects.models
import users.models


def get_random_strings_list():
    res = []
    all_symbols = string.ascii_uppercase + string.ascii_lowercase
    all_symbols += '1234567890'
    for _ in range(100):
        line = ''
        for __ in range(random.randint(50, 100)):
            line += random.choice(all_symbols)
        res.append(line)
    return res


class StaticUrlTest(django.test.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.author = users.models.User.objects.create(
            username='test_user_url',
            email='test_test_123@example.com',
            normalized_email='test_123@yandex.ru',
            is_active=True,
        )
        cls.author.set_password('testsignup123')
        cls.author.clean()
        cls.author.save()

        cls.project = projects.models.Project.objects.create(
            id=1234,
            author=cls.author,
            name='Тестовый проект',
            description='полное описание',
            short_description='краткое описание',
        )

        cls.project.clean()
        cls.project.save()

        cls.client = django.test.Client(cls.author)

    @parameterized.parameterized.expand(
        [
            ('negative_int', [-i for i in range(1, 101)], 404),
            ('negative_string', get_random_strings_list(), 404),
            ('positive', [1234], 200),
        ]
    )
    def test_view_projects(self, name, a, b):
        for i in range(len(a)):
            response = django.test.Client().get(f'/projects/view/{a[i]}')
            self.assertEqual(response.status_code, b)

    def test_create_project_authorized_user(self):
        self.client.login(username='test_user_url', password='testsignup123')
        response = self.client.get(django.urls.reverse('projects:create'))
        self.assertEqual(response.status_code, 200)
        self.client.logout()

    def test_create_project_incognito_user(self):
        response = django.test.Client().get(
            django.urls.reverse('projects:create')
        )
        self.assertEqual(response.status_code, 302)

    def test_positive_redact_project(self):
        self.client.login(username='test_user_url', password='testsignup123')
        response = self.client.get(
            django.urls.reverse('projects:redact', args=[1234])
        )
        self.assertEqual(response.status_code, 200)
        self.client.logout()

    def test_negative_redact_project(self):
        response = django.test.Client().get(
            django.urls.reverse('projects:redact', args=[1234])
        )
        self.assertEqual(response.status_code, 404)

    @classmethod
    def tearDownClass(cls):
        projects.models.Project.objects.all().delete()
        users.models.User.objects.all().delete()
        super().tearDownClass()
