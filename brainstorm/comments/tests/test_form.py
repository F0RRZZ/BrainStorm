import django.test
import django.urls

import comments.models
import projects.models
import users.models


class FormTests(django.test.TestCase):
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

        cls.client = django.test.Client(cls.user_test)

    def test_create_comment(self):
        self.client.login(username='Bob', password='mypassword123')
        all_comment = comments.models.Comment.objects.count()
        data_form = {
            'action': 'leave_comment',
            'text': 'This is a test comment',
        }
        self.client.post(
            django.urls.reverse('projects:view', args=[12]),
            data=data_form,
            follow=True,
        )
        self.assertNotEqual(
            all_comment, comments.models.Comment.objects.count()
        )
        comments.models.Comment.objects.get(
            text='This is a test comment',
        ).delete()

    @classmethod
    def tearDownClass(cls):
        projects.models.Project.objects.all().delete()
        users.models.User.objects.all().delete()
        comments.models.Comment.objects.all().delete()
        return super().tearDownClass()
