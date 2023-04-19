import django.core.validators
import django.db.models
from django.utils.translation import gettext_lazy as _

import projects.models
import rating.managers
import users.models


class ProjectRating(django.db.models.Model):
    class ScoreData:
        MIN = 1
        MAX = 10
        DEFAULT = 5

    project = django.db.models.ForeignKey(
        projects.models.Project,
        verbose_name=_('project'),
        related_name='score_project',
        on_delete=django.db.models.CASCADE,
    )
    user = django.db.models.ForeignKey(
        users.models.User,
        on_delete=django.db.models.CASCADE,
        verbose_name=_('user'),
        related_name='score_project_user',
    )
    score = django.db.models.PositiveSmallIntegerField(
        default=ScoreData.DEFAULT,
        verbose_name=_('score'),
        validators=[
            django.core.validators.MinValueValidator(ScoreData.MIN),
            django.core.validators.MaxValueValidator(ScoreData.MAX),
        ],
    )

    objects = rating.managers.RatingProjectManager()

    class Meta:
        verbose_name = _('rating')
        verbose_name_plural = _('ratings')

    def __str__(self):
        return self.project.name[:15]
