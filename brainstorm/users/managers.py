import django.contrib.auth.models
import django.db.models
import django.shortcuts

import users.models


class UserManager(django.contrib.auth.models.BaseUserManager):
    def get_by_natural_key(self, value):
        if '@' in value:
            return self.get(email__iexact=value)
        return self.get(username__iexact=value)

    def create_user(self, username, email=None, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        email = self.normalize_email(email)
        if email and self.filter(email__iexact=email).exists():
            raise ValueError('User with this email already exists')
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(username, email, password, **extra_fields)

    def get_with_only_username(self, pk):
        return django.shortcuts.get_object_or_404(
            self.filter(
                is_active=True,
            ).only(users.models.User.username.field.name),
            id=pk,
        )

    def user_profile(self):
        return self.get_queryset().only(
            users.models.User.email.field.name,
            users.models.User.username.field.name,
            users.models.User.first_name.field.name,
            users.models.User.last_name.field.name,
            users.models.User.bio.field.name,
            users.models.User.image.field.name,
        )
