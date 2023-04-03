from django import forms
from django.contrib.auth.forms import UserCreationForm

from core.forms import BootstrapFormMixin
from users.models import User


class CustomUserCreationForm(BootstrapFormMixin, UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            User.username.field.name,
            User.email.field.name,
            'password1',
            'password2',
        )


class UserProfileForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = User
        field = [
            User.email.field.name,
            User.username.field.name,
            User.first_name.field.name,
            User.last_name.field.name,
            User.image.field.name,
        ]
