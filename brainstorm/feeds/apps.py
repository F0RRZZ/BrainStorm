import django.apps
from django.utils.translation import ugettext_lazy as _


class FeedsConfig(django.apps.AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'feeds'
    verbose_name = _('feeds')
