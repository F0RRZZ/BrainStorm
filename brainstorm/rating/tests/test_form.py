import django.test
import django.urls

import projects.models
import rating.models
import users.models


class FormsTest(django.test.TestCase):
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

    def test_create_rating(self):
        all_rating = rating.models.ProjectRating.objects.count()
        data_form = {
            'user': self.user,
            'project': self.project,
            'score': 5
        }
        django.test.Client().post(
            django.urls.reverse('projects:view', args=[12]),
            data=data_form,
            follow=True,
        )
        self.assertEqual(
            all_rating,
            rating.models.ProjectRating.objects.count()
        )
        rating.models.ProjectRating.objects.get(
            user=self.user,
            project=self.project
        ).delete()

    def test_redirect_page(self):
        data_form = {
            'user': self.user,
            'project': self.project,
            'score': 5,
        }
        response = django.test.Client().post(
            django.urls.reverse('projects:view', args=[12]),
            data=data_form,
            follow=True,
        )
        self.assertRedirects(
            response,
            django.urls.reverse('projects:view', args=[12])
        )
        rating.models.ProjectRating.objects.get(
            user=self.user,
            project=self.project,
        ).delete()

    @classmethod
    def tearDownClass(cls):
        projects.models.Project.objects.all().delete()
        users.models.User.objects.all().delete()
        rating.models.ProjectRating.objects.all().delete()
        return super().tearDownClass()
