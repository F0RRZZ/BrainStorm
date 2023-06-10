from django.db.models import Avg
import rest_framework.serializers

import projects.models


class ProjectSerializer(rest_framework.serializers.ModelSerializer):
    rating = rest_framework.serializers.SerializerMethodField()

    class Meta:
        model = projects.models.Project
        fields = (
            projects.models.Project.name.field.name,
            projects.models.Project.author.field.name,
            projects.models.Project.short_description.field.name,
            projects.models.Project.description.field.name,
            projects.models.Project.collaborators.field.name,
            projects.models.Project.tags.field.name,
            projects.models.Project.status.field.name,
            projects.models.Project.creation_date.field.name,
            projects.models.Project.update_date.field.name,
            'rating',
        )

    def get_rating(self, obj):
        return round(
            obj.score_project.aggregate(Avg('score'))['score__avg'], 1
        )
