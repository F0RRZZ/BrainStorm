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
    contact = django.db.models.TextField('информация о контактах', max_length=150, blank=True,)
    about = django.db.models.TextField('информация о пользователе', blank=True,)
    answer = django.db.models.TextField('ответ автора проекта', blank=True,)
    viewed = django.db.models.BooleanField('просмотрено', default=False,)
    creation_date = django.db.models.DateTimeField('дата создания', auto_now_add=True,)
    status = django.db.models.CharField(
        'статус заявки',
        max_length=20,
        choices=Status.choices,
        default=Status.IN_QUEUE,
    )

    objects = collaboration.managers.CollaborationRequestManager()
