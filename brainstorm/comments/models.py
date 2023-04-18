import django.db.models

import comments.managers
import projects.models
import users.models


class Comment(django.db.models.Model):
    objects = comments.managers.CommentsManager()

    project = django.db.models.ForeignKey(
        projects.models.Project,
        verbose_name='проект',
        related_name='comments',
        on_delete=django.db.models.CASCADE,
        help_text='Какому проекту принадлежит комментарий',
    )
    user = django.db.models.ForeignKey(
        users.models.User,
        on_delete=django.db.models.CASCADE,
        verbose_name='пользователь',
        related_name='comments',
    )
    text = django.db.models.TextField(
        'комментарий',
        help_text='Оставить комментарий',
    )
    creation_date = django.db.models.DateTimeField(
        'дата создания',
        auto_now_add=True,
    )
    update_date = django.db.models.DateTimeField(
        'дата изменения',
        auto_now=True,
    )

    class Meta:
        ordering = [
            f'-creation_date',
        ]
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'

    def __str__(self):
        return self.text[:15]
