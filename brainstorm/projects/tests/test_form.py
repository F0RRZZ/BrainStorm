import django.test
from django.utils.translation import gettext_lazy as _

import projects.forms
import projects.models
import users.models


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
        self.assertEqual(name_label, 'Имя')

    def test_short_description_label_correct(self):
        short_description_label = self.form.fields['short_description'].label
        self.assertEqual(short_description_label, _('Краткое описание'))

    def test_description_label_correct(self):
        description_label = self.form.fields['description'].label
        self.assertEqual(description_label, _('Полное описание'))

    def test_status_label_correct(self):
        status_label = self.form.fields['status'].label
        self.assertEqual(status_label, _('Статус'))

    def test_tags_label_correct(self):
        tags_label = self.form.fields['tags'].label
        self.assertEqual(tags_label, _('Теги'))

    @classmethod
    def tearDownClass(cls):
        projects.models.Project.objects.all().delete()
        users.models.User.objects.all().delete()
        super().tearDownClass()
