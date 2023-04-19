import django.db.models
from django.utils.translation import gettext_lazy as _

import comments.managers
import projects.models
import users.models


class Comment(django.db.models.Model):
    objects = comments.managers.CommentsManager()

    project = django.db.models.ForeignKey(
        projects.models.Project,
        verbose_name=_('project'),
        related_name='comments',
        on_delete=django.db.models.CASCADE,
    )
    user = django.db.models.ForeignKey(
        users.models.User,
        on_delete=django.db.models.CASCADE,
        verbose_name=_('user'),
        related_name='comments',
    )
    text = django.db.models.TextField(
        _('comment'),
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
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
        ordering = [
            '-creation_date',
        ]

    def __str__(self):
        return self.text[:15]
