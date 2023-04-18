import django.apps
from django.utils.translation import ugettext_lazy as _


class AboutConfig(django.apps.AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'about'
    verbose_name = _('about_project')
