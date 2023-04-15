import django.test

import users.forms


class UserCreationFormTests(django.test.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.form = users.forms.CustomUserCreationForm()

    def test_email_label(self):
        email_label = UserCreationFormTests.form.fields['email'].label
        self.assertEqual(email_label, 'Почта')

    def test_email_help_text(self):
        email_help_text = (
            UserCreationFormTests.form.fields['email'].help_text
        )
        self.assertEqual(email_help_text, 'Электронная почта')

    def test_username_label(self):
        username_label = UserCreationFormTests.form.fields['username'].label
        self.assertEqual(username_label, 'Имя пользователя')

    def test_username_help_text(self):
        username_help_text = (
            UserCreationFormTests.form.fields['username'].help_text
        )
        self.assertEqual(
            username_help_text,
            'Допускаются только буквы, цифры, дефис и нижнее подчеркивание',
        )

    def test_password_label(self):
        username_label = UserCreationFormTests.form.fields['password1'].label
        self.assertEqual(username_label, 'Password')

    def test_password_help_text(self):
        password_help_text = (
            UserCreationFormTests.form.fields['password2'].help_text
        )
        self.assertEqual(
            password_help_text,
            'Enter the same password as before, for verification.'
        )
