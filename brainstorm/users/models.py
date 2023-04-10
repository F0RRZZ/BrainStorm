import os
import re

import django.contrib.auth.models
import django.db.models

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
    username = django.db.models.CharField(
        'username',
        max_length=100,
        unique=True,
        help_text='Имя пользователя',
    )
    bio = django.db.models.TextField(
        'bio',
        max_length=1000,
        default='',
        help_text='О себе',
    )
    first_name = django.db.models.CharField(
        'first name',
        max_length=100,
        null=True,
        blank=True,
        help_text='Имя',
    )
    last_name = django.db.models.CharField(
        'last name',
        max_length=100,
        null=True,
        blank=True,
        help_text='Фамилия',
    )
    email = django.db.models.EmailField(
        'email address',
        max_length=254,
        unique=True,
        help_text='Электронная почта',
    )
    normalized_email = NormalizedEmailField(
        'normalized email address',
        unique=True,
        help_text='Нормализованная электронная почта',
    )
    date_joined = django.db.models.DateTimeField(
        'date joined',
        auto_now=True,
        help_text='Дата регистрации',
    )
    is_active = django.db.models.BooleanField(
        'active',
        default=False,
        help_text='Активен',
    )
    is_staff = django.db.models.BooleanField(
        'staff',
        default=False,
        help_text='Персонал',
    )
    is_superuser = django.db.models.BooleanField(
        'superuser',
        default=False,
        help_text='Суперпользователь',
    )

    def get_image_filename(self, filename):
        ext = os.path.splitext(filename)[-1]
        return 'avatars/user_{}{}'.format(self.id, ext)

    image = django.db.models.ImageField(
        'profile picture',
        upload_to=get_image_filename,
        null=True,
        blank=True,
        help_text='Аватарка',
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = users.managers.UserManager()

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def natural_key(self):
        return self.username

    def save(self, *args, **kwargs):
        self.normalized_email = self.normalized_email or self.email
        super(User, self).save(*args, **kwargs)
