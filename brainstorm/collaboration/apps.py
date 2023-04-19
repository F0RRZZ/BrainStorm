import django.apps
from django.utils.translation import ugettext_lazy as _


class CollaborationConfig(django.apps.AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'collaboration'
    verbose_name = _('collaboration')
