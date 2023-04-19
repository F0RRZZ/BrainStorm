import re

import django.contrib.auth.forms
import django.forms
from django.utils.translation import gettext_lazy as _

import core.forms
import users.models

PASSWORD1_FIELD_NAME = 'password1'
PASSWORD2_FIELD_NAME = 'password2'


class CustomUserCreationForm(
    core.forms.BootstrapFormMixin, django.contrib.auth.forms.UserCreationForm
):
    password1 = django.forms.CharField(
        label=_('password'),
        strip=False,
        widget=django.forms.PasswordInput(
            attrs={'autocomplete': 'new-password'}, render_value=False
        ),
    )
    password2 = django.forms.CharField(
        label=_('password_again'),
        widget=django.forms.PasswordInput(
            attrs={'autocomplete': 'new-password'}, render_value=False
        ),
        strip=False,
        help_text=_('type_password_again_for_confirmation'),
    )

    class Meta:
        model = users.models.User
        fields = (
            users.models.User.username.field.name,
            users.models.User.email.field.name,
            PASSWORD1_FIELD_NAME,
            PASSWORD2_FIELD_NAME,
        )

    def clean_username(self):
        username = self.cleaned_data[users.models.User.username.field.name]
        if not re.match(r'^[\w-]+$', username):
            raise django.forms.ValidationError(_('incorrect_username'))
        return username


class UserProfileForm(core.forms.BootstrapFormMixin, django.forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields[users.models.User.bio.field.name].required = False

    class Meta:
        model = users.models.User
        fields = [
            users.models.User.email.field.name,
            users.models.User.username.field.name,
            users.models.User.first_name.field.name,
            users.models.User.last_name.field.name,
            users.models.User.bio.field.name,
            users.models.User.image.field.name,
        ]
