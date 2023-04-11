import django.db.models

import projects.models
import users.models

CREATION_DATE_FIELD_NAME = 'creation_date'


class Comment(django.db.models.Model):
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
            f'-{CREATION_DATE_FIELD_NAME}',
        ]
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'

    def __str__(self):
        return self.text[:15]
