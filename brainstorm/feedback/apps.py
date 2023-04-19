import django.apps
from django.utils.translation import ugettext_lazy as _


class FeedbackConfig(django.apps.AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'feedback'
    verbose_name = _('feedbacks')
