import django.apps
from django.utils.translation import ugettext_lazy as _


class CommentsConfig(django.apps.AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'comments'
    verbose_name = _('comments')
