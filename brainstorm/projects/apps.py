import django.apps
from django.utils.translation import ugettext_lazy as _


class ProjectsConfig(django.apps.AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'projects'
    verbose_name = _('projects')
