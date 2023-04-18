import os
import re

import django.contrib.auth.models
import django.db.models
from django.utils.translation import gettext_lazy as _

import core.utils
import users.managers


class NormalizedEmailField(django.db.models.EmailField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_prep_value(self, value):
        if value:
            value = re.sub(r'(?i)(\<.*?\>)', '', value)

            if '@ya.ru' in value:
                value = value.split('@')[0] + '@yandex.ru'
            if '+' in value:
                value = (
                    f'{value.split("@")[0].split("+")[0]}@'
                    f'{value.split("@")[-1]}'
                )

            value = value.lower()

            if '@gmail.com' in value:
                username, domain = value.split('@')
                username = username.replace('.', '')
                value = f'{username}@{domain}'

            if '@yandex.ru' in value:
                username, domain = value.split('@')
                username = username.replace('.', '-')
                value = f'{username}@{domain}'

        return value


class User(
    django.contrib.auth.models.AbstractBaseUser,
    django.contrib.auth.models.PermissionsMixin,
    core.utils.ImageMixin,
):
    DEFAULT_IMAGE = 'images/user_default.jpg'

    username = django.db.models.CharField(
        _('username'),
        max_length=100,
        help_text=(_('only_letters_defis_and_underline')),
        unique=True,
    )
    bio = django.db.models.TextField(
        _('user_bio'),
        max_length=1000,
        default='',
    )
    first_name = django.db.models.CharField(
        _('name'),
        max_length=100,
        null=True,
        blank=True,
    )
    last_name = django.db.models.CharField(
        _('last_name'),
        max_length=100,
        null=True,
        blank=True,
    )
    email = django.db.models.EmailField(
        _('user_email'),
        max_length=254,
        unique=True,
    )
    normalized_email = NormalizedEmailField(
        _('normalized_email'),
        unique=True,
    )
    date_joined = django.db.models.DateTimeField(
        _('date_joined'),
        auto_now=True,
    )
    is_active = django.db.models.BooleanField(
        _('active'),
        default=False,
    )
    is_staff = django.db.models.BooleanField(
        _('staff'),
        default=False,
    )
    is_superuser = django.db.models.BooleanField(
        _('superuser'),
        default=False,
    )

    def get_image_filename(self, filename):
        ext = os.path.splitext(filename)[-1]
        return 'avatars/user_{}{}'.format(self.id, ext)

    image = django.db.models.ImageField(
        _('avatar'),
        upload_to=get_image_filename,
        null=True,
        blank=True,
    )

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [
        EMAIL_FIELD,
    ]

    objects = users.managers.UserManager()

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def natural_key(self):
        return self.username

    def save(self, *args, **kwargs):
        self.normalized_email = self.normalized_email or self.email
        super(User, self).save(*args, **kwargs)
