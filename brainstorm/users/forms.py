from django import forms
from django.contrib.auth.forms import UserCreationForm

from core.forms import BootstrapFormMixin
from users.models import User


class CustomUserCreationForm(BootstrapFormMixin, UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
