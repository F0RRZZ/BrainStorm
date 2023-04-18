import os

import django.core.files.uploadedfile as uploadedfile
import django.test
import django.urls

import feedback.models


class FeedbackViewTests(django.test.TestCase):
    def setUp(self) -> None:
        self.form_data = {
            'subject': 'subject',
            'text': 'text',
            'email': 'ex@ex.com',
        }

    def test_feedback_page_context(self):
        response = django.test.Client().get(
            django.urls.reverse('feedback:feedback')
        )
        self.assertIn('form', response.context)

    def test_create_feedback(self):
        feedbacks_count = feedback.models.Feedback.objects.count()
        django.test.Client().post(
            django.urls.reverse('feedback:feedback'),
            data=self.form_data,
            follow=True,
        )
        self.assertEqual(
            feedback.models.Feedback.objects.count(), feedbacks_count + 1
        )
        self.assertTrue(
            feedback.models.Feedback.objects.filter(text='text').exists()
        )

    def test_redirect(self):
        response = django.test.Client().post(
            django.urls.reverse('feedback:feedback'),
            data=self.form_data,
            follow=True,
        )
        self.assertRedirects(response, django.urls.reverse('feedback:success'))

    def test_file_upload(self):
        with open('test_file.txt', 'w') as f:
            f.write('test')
        with open('test_file.txt', 'rb') as f:
            form_data = self.form_data
            form_data['files'] = uploadedfile.SimpleUploadedFile(
                f.name, f.read()
            )
            django.test.Client().post(
                django.urls.reverse('feedback:feedback'),
                data=form_data,
                follow=True,
            )
            self.assertTrue(os.path.exists('uploads/1/test_file.txt'))
        os.remove('uploads/1/test_file.txt')
        os.remove('test_file.txt')
        os.rmdir('uploads/1/')
