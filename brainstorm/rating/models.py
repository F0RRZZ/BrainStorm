import django.core.validators
import django.db.models

import projects.models
import rating.managers
import users.models


class ProjectRating(django.db.models.Model):
    objects = rating.managers.RatingProjectManager()

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
