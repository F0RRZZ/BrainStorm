import django.db.models

import core.utils


def directory_path(instance, filename):
    path = f'{instance.project.name}_{instance.project.author.id}'
    return f'{path}/{filename}'


class ProjectImage(django.db.models.Model, core.utils.ImageMixin):
    image = django.db.models.ImageField(
        'превью',
        upload_to=directory_path,
    )

    class Meta:
        abstract = True
