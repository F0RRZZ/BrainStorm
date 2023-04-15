import django.db.models


class RatingProjectManager(django.db.models.Manager):
    def get_avg_rating(self, project_id):
        return (
            self.filter(project_id=project_id)
            .aggregate(avg_rating=django.db.models.Avg('score'))
            .get('avg_rating') or '?'
        )
