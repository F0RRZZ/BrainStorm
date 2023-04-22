import django.core.exceptions
import django.test

import projects.models
import rating.models
import users.models


class ModelsTest(django.test.TestCase):
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

    def test_validation_score(self):
        with self.assertRaises(django.core.exceptions.ValidationError):
            self.rating_project = rating.models.ProjectRating.objects.create(
                id=12,
                project=self.project,
                user=self.user_test,
                score=20,
            )
            self.rating_project.full_clean()
        self.rating_project.delete()

    def test_create_rating(self):
        all_score = rating.models.ProjectRating.objects.count()
        self.rating_project = rating.models.ProjectRating.objects.create(
            id=13,
            project=self.project,
            user=self.user_test,
            score=3,
        )
        self.rating_project.clean()
        self.rating_project.save()
        self.assertNotEqual(
            rating.models.ProjectRating.objects.count(), all_score
        )

    @classmethod
    def tearDownClass(cls):
        projects.models.Project.objects.all().delete()
        users.models.User.objects.all().delete()
        rating.models.ProjectRating.objects.all().delete()
        return super().tearDownClass()
