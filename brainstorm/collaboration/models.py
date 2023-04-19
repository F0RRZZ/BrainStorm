import ckeditor.fields
import django.db.models
from django.utils.translation import gettext_lazy as _

import collaboration.managers
import projects.models
import users.models


class CollaborationRequest(django.db.models.Model):
    class Status(django.db.models.TextChoices):
        IN_QUEUE = ('in_queue', _('in_queue'))
        REJECTED = ('rejected', _('rejected'))
        ADOPTED = ('adopted', _('adopted'))

    project = django.db.models.ForeignKey(
        projects.models.Project,
        on_delete=django.db.models.CASCADE,
        related_name='collaboration_requests',
    )
    user = django.db.models.ForeignKey(
        users.models.User,
        on_delete=django.db.models.CASCADE,
        related_name='collaboration_requests',
    )
    contact = ckeditor.fields.RichTextField(
        _('contacts'),
        blank=True,
    )
    about = ckeditor.fields.RichTextField(
        _('about_user'),
        blank=True,
    )
    answer = django.db.models.TextField(
        _('answer__noun'),
        blank=True,
        help_text=_('answer_of_project_author'),
    )
    creation_date = django.db.models.DateTimeField(
        _('creation_date'),
        auto_now_add=True,
    )
    status = django.db.models.CharField(
        _('status'),
        max_length=20,
        choices=Status.choices,
        default=Status.IN_QUEUE,
    )

    objects = collaboration.managers.CollaborationRequestManager()

    class Meta:
        verbose_name = _('collaboration').lower()
        verbose_name_plural = _('collaborations').lower()
