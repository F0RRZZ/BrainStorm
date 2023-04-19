import django.apps
from django.utils.translation import ugettext_lazy as _


class UsersConfig(django.apps.AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    verbose_name = _('users')

    def ready(self):
        import users.signals
