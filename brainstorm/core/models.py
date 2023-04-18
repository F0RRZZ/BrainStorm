import django.db.models
from django.utils.translation import gettext_lazy as _

import core.utils


def directory_path(instance, filename):
    path = f'project_previews/project_{instance.project.id}'
    return f'{path}/{filename}'


class ProjectImage(django.db.models.Model, core.utils.ImageMixin):
    image = django.db.models.ImageField(
        _('preview'),
        upload_to=directory_path,
    )

    class Meta:
        abstract = True
