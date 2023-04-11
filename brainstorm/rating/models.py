import django.core.validators
import django.db.models

import comments.models
import projects.models
import users.models


class ProjectRating(django.db.models.Model):
    class ScoreData:
        MIN = 1
        MAX = 10
        DEFAULT = 5

    project = django.db.models.ForeignKey(
        projects.models.Project,
        verbose_name='проект',
        related_name='score_project',
        on_delete=django.db.models.CASCADE,
        help_text='Какому проекту принадлежит оценка',
    )
    user = django.db.models.ForeignKey(
        users.models.User,
        on_delete=django.db.models.CASCADE,
        verbose_name='пользователь',
        related_name='score_project_user',
    )
    score = django.db.models.PositiveSmallIntegerField(
        default=ScoreData.DEFAULT,
        verbose_name='оценка проекта',
        validators=[
            django.core.validators.MinValueValidator(ScoreData.MIN),
            django.core.validators.MaxValueValidator(ScoreData.MAX),
        ],
    )

    class Meta:
        verbose_name = 'рейтинг проетка'
        verbose_name_plural = 'рейтинг проектов'

    def __str__(self):
        return self.project.name[:15]


class CommentRating(django.db.models.Model):
    user = django.db.models.ForeignKey(
        users.models.User,
        on_delete=django.db.models.CASCADE,
        verbose_name='пользователь',
        related_name='score_comment_user',
    )
    comment = django.db.models.ForeignKey(
        comments.models.Comment,
        verbose_name='комментарий',
        related_name='score_comment',
        on_delete=django.db.models.CASCADE,
        help_text='Какому комментарию принадлежит оценка',
    )
    score = django.db.models.PositiveSmallIntegerField(
        verbose_name='оценка проекта',
        validators=[
            django.core.validators.MinValueValidator(1),
            django.core.validators.MaxValueValidator(10),
        ],
    )

    class Meta:
        verbose_name = 'рейтинг комментария'
        verbose_name_plural = 'рейтинг комментариев'

    def __str__(self):
        return self.comment.text[:15]
