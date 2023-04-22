import django.test
from django.utils.translation import gettext_lazy as _

import users.forms


class UserCreationFormTests(django.test.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.form = users.forms.CustomUserCreationForm()

    def test_email_label(self):
        email_label = UserCreationFormTests.form.fields['email'].label
        self.assertEqual(email_label, _('User_email'))

    def test_username_label(self):
        username_label = UserCreationFormTests.form.fields['username'].label
        self.assertEqual(username_label, 'Имя пользователя')

    def test_username_help_text(self):
        username_help_text = UserCreationFormTests.form.fields[
            'username'
        ].help_text
        self.assertEqual(
            username_help_text,
            _('only_letters_defis_and_underline'),
        )

    def test_password_label(self):
        password_label = UserCreationFormTests.form.fields['password1'].label
        self.assertEqual(password_label, 'пароль')

    def test_password_confirm_label(self):
        password_confirm_label = UserCreationFormTests.form.fields[
            'password2'
        ].label
        self.assertEqual(password_confirm_label, _('password_again'))

    def test_password_confirm_help_text(self):
        password_confirm_help_text = UserCreationFormTests.form.fields[
            'password2'
        ].help_text
        self.assertEqual(
            password_confirm_help_text,
            _('type_password_again_for_confirmation'),
        )
