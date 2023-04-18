import django.apps
from django.utils.translation import ugettext_lazy as _


class TagsConfig(django.apps.AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tags'
    verbose_name = _('tags')
