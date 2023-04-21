import django.test

import feedback.forms


class FormTests(django.test.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.form = feedback.forms.FeedbackForm()

    def test_text_label(self):
        text_label = FormTests.form.fields['text'].label
        self.assertEqual(text_label, 'Message')

    def test_email_label(self):
        email_label = FormTests.form.fields['email'].label
        self.assertEqual(email_label, 'user_email')

    def test_email_help_text(self):
        email_help_text = FormTests.form.fields['email'].help_text
        self.assertEqual(
            email_help_text,
            'type_email_on_what_answer_will_be_sent__lowercase',
        )

    def test_file_upload_label(self):
        file_upload_label = FormTests.form.fields['files'].label
        self.assertEqual(file_upload_label, 'files')

    def test_file_upload_text(self):
        file_upload_text = FormTests.form.fields['files'].help_text
        self.assertEqual(
            file_upload_text, 'add_some_files_if_necessary__lowercase'
        )
