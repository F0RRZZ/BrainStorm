import django.contrib.auth.backends

import users.models


class NormalizedEmailAuthBackend(django.contrib.auth.backends.ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(
                django.contrib.auth.backends.UserModel.USERNAME_FIELD,
            )
        try:
            user = users.models.User.objects.get(normalized_email=username)
        except users.models.User.DoesNotExist:
            django.contrib.auth.backends.UserModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(
                user
            ):
                return user
