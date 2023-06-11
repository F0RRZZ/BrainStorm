import rest_framework.fields
from django.db.models import Avg
import rest_framework.serializers

import api.v1.users.serializers
import comments.models
import projects.models
import tags.models


class CommentSerializer(rest_framework.serializers.ModelSerializer):
    user = api.v1.users.serializers.UserSerializer()

    class Meta:
        model = comments.models.Comment
        fields = (
            comments.models.Comment.user.field.name,
            comments.models.Comment.text.field.name,
            comments.models.Comment.creation_date.field.name,
            comments.models.Comment.update_date.field.name,
        )


class TagSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = tags.models.Tag
        fields = (
            tags.models.Tag.name.field.name,
            tags.models.Tag.description.field.name,
        )


class ProjectSerializer(rest_framework.serializers.ModelSerializer):
    rating = rest_framework.serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)

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
            'comments',
        )

    def get_rating(self, obj):
        return round(
            obj.score_project.aggregate(Avg('score'))['score__avg'], 1
        )
