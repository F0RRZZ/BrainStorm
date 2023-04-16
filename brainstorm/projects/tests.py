import random
import string

import django.core.exceptions
import django.core.files.uploadedfile
import django.test
import django.urls
from parameterized import parameterized

import projects.forms
import projects.models
import tags.models
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

        cls.user_on_site = django.test.Client(cls.author)

    @parameterized.expand(
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
        self.assertEqual(response.status_code, 302)

    @classmethod
    def tearDownClass(cls):
        projects.models.Project.objects.all().delete()
        users.models.User.objects.all().delete()
        super().tearDownClass()


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


class ContextTests(django.test.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.author = users.models.User.objects.create(
            username='test_user_context',
            email='test_my_new@example.com',
            normalized_email='test_new@yandex.ru',
            is_active=True,
        )
        cls.author.set_password('testsignup123')
        cls.author.clean()
        cls.author.save()

        cls.project = projects.models.Project.objects.create(
            id=25,
            author=cls.author,
            name='Тестовый проект для контекса',
            description='полное описание',
            short_description='краткое описание',
        )

        cls.project.clean()
        cls.project.save()

        cls.test_tag = tags.models.Tag.objects.create(
            id=15,
            name='Автомобили',
        )
        cls.test_tag.save()

        image_path = 'projects/fixtures/cat.jpg'

        images = [
            'projects/fixtures/dog_1.jpg',
            'projects/fixtures/dog_2.jpg',
            'projects/fixtures/dog_3.jpg',
        ]

        cls.preview = projects.models.Preview.objects.create(
            project=cls.project
        )
        cls.preview.save()

        cls.preview.image = django.core.files.uploadedfile.SimpleUploadedFile(
            name='cat.jpg',
            content=open(image_path, 'rb').read(),
            content_type='image/jpeg',
        )

        for image in images:
            cls.gallery = projects.models.ImagesGallery.objects.create(
                project=cls.project
            )

            cls.gallery.image = (
                django.core.files.uploadedfile.SimpleUploadedFile(
                    name=image.split('/')[-1],
                    content=open(image, 'rb').read(),
                    content_type='image/jpeg',
                )
            )

            cls.gallery.save()

        cls.project.tags.add(cls.test_tag.pk)

        cls.user_on_site = django.test.Client(cls.author)

        cls.user_on_site.login(
            username='test_user_context', password='testsignup123'
        )

    def test_form_in_project_create_context(self):
        response = self.user_on_site.get(
            django.urls.reverse('projects:create')
        )
        self.assertIn('form', response.context)

    def test_form_in_context_is_projectform(self):
        response = self.user_on_site.get(
            django.urls.reverse('projects:create')
        )
        self.assertIsInstance(
            response.context['form'], projects.forms.ProjectForm
        )

    def test_project_view_context(self):
        response = django.test.Client().get(
            django.urls.reverse('projects:view', args=[25])
        )
        self.assertIn('project', response.context)

    def test_project_view_with_tags_context(self):
        response = django.test.Client().get(
            django.urls.reverse('projects:view', args=[25])
        )
        project = response.context['project']
        self.assertTrue(project.tags.get(name='Автомобили'))

    def test_project_view_with_preview_context(self):
        response = django.test.Client().get(
            django.urls.reverse('projects:view', args=[25])
        )
        project = response.context['project']
        self.assertTrue(project.preview)

    def test_project_view_with_images_gallery_context(self):
        response = django.test.Client().get(
            django.urls.reverse('projects:view', args=[25])
        )
        project = response.context['project']
        for image in project.images_gallery.all():
            self.assertIsNotNone(image)

    @classmethod
    def tearDownClass(cls):
        projects.models.Project.objects.all().delete()
        projects.models.Preview.objects.all().delete()
        projects.models.ImagesGallery.objects.all().delete()
        users.models.User.objects.all().delete()
        tags.models.Tag.objects.all().delete()
        super().tearDownClass()


class FormsTests(django.test.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.author = users.models.User.objects.create(
            username='test_user_form',
            email='test_my_form@example.com',
            normalized_email='test_form@yandex.ru',
            is_active=True,
        )
        cls.author.set_password('testsignup123')
        cls.author.clean()
        cls.author.save()

        cls.form = projects.forms.ProjectForm()

        cls.user_on_site = django.test.Client(cls.author)

        cls.user_on_site.login(
            username='test_user_form', password='testsignup123'
        )

    def test_name_label_correct(self):
        name_label = self.form.fields['name'].label
        self.assertEqual(name_label, 'Название')

    def test_short_description_label_correct(self):
        short_description_label = self.form.fields['short_description'].label
        self.assertEqual(short_description_label, 'Краткое описание')

    def test_description_label_correct(self):
        description_label = self.form.fields['description'].label
        self.assertEqual(description_label, 'Описание')

    def test_collaborators_label_correct(self):
        collaborators_label = self.form.fields['collaborators'].label
        self.assertEqual(collaborators_label, 'Коллабораторы')

    def test_status_label_correct(self):
        status_label = self.form.fields['status'].label
        self.assertEqual(status_label, 'Статус')

    def test_tags_label_correct(self):
        tags_label = self.form.fields['tags'].label
        self.assertEqual(tags_label, 'Теги')

    @classmethod
    def tearDownClass(cls):
        projects.models.Project.objects.all().delete()
        users.models.User.objects.all().delete()
        super().tearDownClass()
