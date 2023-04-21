import django.core.exceptions
import django.test

import comments.models
import projects.models
import users.models


class ModelTest(django.test.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = users.models.User.objects.create(
            username='Test_user_for_model',
            email='test_example@gmail.com',
            normalized_email='test_test@gmail.com',
            is_active=True,
        )
        cls.user.set_password('aboba123')
        cls.user.clean()
        cls.user.save()
        cls.project = projects.models.Project.objects.create(
            id=12,
            name='Test_project',
            author=cls.user,
            description='Для описания',
            short_description='Супер кратко',
        )
        cls.project.clean()
        cls.project.save()

        cls.user_test = users.models.User.objects.create(
            username='Bob',
            email='bobAbd2l@gmai.ru',
            is_active=True,
        )
        cls.user_test.set_password('mypassword123')
        cls.user_test.clean()
        cls.user_test.save()

    def test_create_comment(self):
        all_comment = comments.models.Comment.objects.count()
        self.test_comment = comments.models.Comment.objects.create(
            user=self.user_test,
            project=self.project,
            text='У вас тестовый проект',
        )
        self.test_comment.clean()
        self.test_comment.save()
        self.assertNotEqual(
            comments.models.Comment.objects.count(),
            all_comment
        )
        self.test_comment.delete()

    @classmethod
    def tearDownClass(cls):
        projects.models.Project.objects.all().delete()
        users.models.User.objects.all().delete()
        comments.models.Comment.objects.all().delete()
        return super().tearDownClass()
