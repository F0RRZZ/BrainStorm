import django.core
import django.test
import django.urls

import projects.models
import tags.models
import users.models


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
