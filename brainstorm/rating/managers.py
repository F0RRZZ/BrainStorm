import django.db.models

import rating.models


class RatingProjectManager(django.db.models.Manager):
    def get_avg_rating(self, project_id):
        avg = (
            self.filter(project_id=project_id)
            .aggregate(
                avg_rating=django.db.models.Avg(
                    rating.models.ProjectRating.score.field.name
                )
            )
            .get('avg_rating')
        )
        if avg is None:
            return '?'
        if avg % 1 == 0:
            return int(avg)
        return round(avg, 1)
