import django.db.models
import rest_framework.serializers

import api.v1.comments.serializers
import api.v1.tags.serializers
import projects.models


class ProjectSerializer(rest_framework.serializers.ModelSerializer):
    rating = rest_framework.serializers.SerializerMethodField()
    comments = api.v1.comments.serializers.CommentSerializer(
        many=True, read_only=True
    )
    tags = api.v1.tags.serializers.TagSerializer(many=True, read_only=True)

    class Meta:
        model = projects.models.Project
        fields = (
            'id',
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
            'comments',
        )

    def get_rating(self, obj):
        return round(
            obj.score_project.aggregate(django.db.models.Avg('score'))[
                'score__avg'
            ],
            1,
        )
