import django.test

import projects.models
import users.models


class ModelsTests(django.test.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.author = users.models.User.objects.create(
            username='test_user_model',
            email='test@example.com',
            normalized_email='test@yandex.ru',
            is_active=True,
        )
        cls.author.set_password('testsignup123')
        cls.author.clean()
        cls.author.save()

    def test_create_project(self):
        project_count = projects.models.Project.objects.count()
        self.project = projects.models.Project.objects.create(
            id=1234,
            author=self.author,
            name='Проверочный проект',
            description='полное описание',
            short_description='краткое описание',
        )
        self.project.clean()
        self.project.save()
        self.assertNotEqual(
            projects.models.Project.objects.count(), project_count
        )
        self.project.delete()

    @classmethod
    def tearDownClass(cls):
        projects.models.Project.objects.all().delete()
        users.models.User.objects.all().delete()
        super().tearDownClass()
