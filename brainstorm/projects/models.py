import ckeditor.fields
import django.db.models
import django.utils.safestring
from django.utils.translation import gettext_lazy as _

import core.models
import core.utils
import projects.managers
import tags.models
import users.models


class Project(django.db.models.Model):
    objects = projects.managers.ProjectManager()

    class Status(django.db.models.TextChoices):
        IDEA = ('idea', _('idea'))
        DEVELOPMENT = ('development', _('in_develop'))
        READY = ('ended', _('ended'))

    author = django.db.models.ForeignKey(
        users.models.User,
        on_delete=django.db.models.CASCADE,
        related_name='projects',
        verbose_name='автор',
    )

    name = django.db.models.CharField(
        _('name'),
        max_length=150,
    )
    short_description = ckeditor.fields.RichTextField(
        _('short_description'),
    )
    description = ckeditor.fields.RichTextField(
        _('full_description'),
    )
    collaborators = django.db.models.ManyToManyField(
        users.models.User,
        verbose_name=_('collaborators'),
        related_name='colleagues',
    )
    tags = django.db.models.ManyToManyField(
        tags.models.Tag,
        verbose_name=_('tags'),
        related_name='projects',
        help_text=_('5_tags_maximum__lowercase'),
    )
    published = django.db.models.BooleanField(
        _('published'),
        default=True,
    )
    in_archive = django.db.models.BooleanField(
        _('in_archive'),
        default=False,
    )
    status = django.db.models.CharField(
        _('status'),
        max_length=20,
        choices=Status.choices,
        default=Status.IDEA,
    )
    creation_date = django.db.models.DateTimeField(
        _('creation_date'),
        auto_now_add=True,
    )
    update_date = django.db.models.DateTimeField(
        _('update_date'),
        auto_now=True,
    )

    class Meta:
        verbose_name = 'проект'
        verbose_name_plural = 'проекты'

    def __str__(self):
        return self.name[:15]

    def image_tmb(self):
        if self.preview:
            image_url = self.preview.get_image_300x300.url
            return django.utils.safestring.mark_safe(
                f'<img src="{image_url}" width="50" height="50">'
            )
        return _('no_photo')

    image_tmb.short_description = _('preview')
    image_tmb.allow_tags = True


class Preview(core.models.ProjectImage):
    project = django.db.models.OneToOneField(
        Project,
        on_delete=django.db.models.CASCADE,
        related_name='preview',
    )

    class Meta:
        verbose_name = 'превью'
        verbose_name_plural = 'превьюшки'

    def __str__(self):
        return self.image.url


class ImagesGallery(core.models.ProjectImage):
    project = django.db.models.ForeignKey(
        Project,
        on_delete=django.db.models.CASCADE,
        related_name='images_gallery',
    )

    class Meta:
        verbose_name = 'галерея'
        verbose_name_plural = 'галереи'

    def __str__(self):
        return self.image.url
