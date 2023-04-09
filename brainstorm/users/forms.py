import re

import django.forms
import django.contrib.auth.forms

import core.forms
from users.models import User


class CustomUserCreationForm(
    core.forms.BootstrapFormMixin, django.contrib.auth.forms.UserCreationForm
):
    email = django.forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            User.username.field.name,
            User.email.field.name,
            'password1',
            'password2',
        )

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.match(r'^[\w-]+$', username):
            raise django.forms.ValidationError('Недопустимое имя пользователя')
        return username


class UserProfileForm(core.forms.BootstrapFormMixin, django.forms.ModelForm):
    class Meta:
        model = User
        fields = [
            User.email.field.name,
            User.username.field.name,
            User.first_name.field.name,
            User.last_name.field.name,
            User.image.field.name,
        ]


class LoginForm(
    core.forms.BootstrapFormMixin,
    django.contrib.auth.forms.AuthenticationForm,
):
    pass


class PasswordChangeForm(
    core.forms.BootstrapFormMixin,
    django.contrib.auth.forms.PasswordChangeForm,
):
    pass


class PasswordResetForm(
    core.forms.BootstrapFormMixin,
    django.contrib.auth.forms.PasswordResetForm,
):
    pass
