import django.test

import feedback.forms


class FormTests(django.test.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.form = feedback.forms.FeedbackForm()

    def test_text_label(self):
        text_label = FormTests.form.fields['text'].label
        self.assertEqual(text_label, 'Текст')

    def test_text_help_text(self):
        text_help_text = FormTests.form.fields['text'].help_text
        self.assertEqual(text_help_text, 'содержание письма')

    def test_email_label(self):
        email_label = FormTests.form.fields['email'].label
        self.assertEqual(email_label, 'Почта')

    def test_email_help_text(self):
        email_help_text = FormTests.form.fields['email'].help_text
        self.assertEqual(email_help_text, 'введите свою почту')

    def test_file_upload_label(self):
        file_upload_label = FormTests.form.fields['files'].label
        self.assertEqual(file_upload_label, 'Файлы')

    def test_file_upload_text(self):
        file_upload_text = FormTests.form.fields['files'].help_text
        self.assertEqual(file_upload_text, 'Приложите файлы')
