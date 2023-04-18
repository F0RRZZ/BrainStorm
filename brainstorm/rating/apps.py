import django.apps
from django.utils.translation import ugettext_lazy as _


class RatingConfig(django.apps.AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rating'
    verbose_name = _('rating')
