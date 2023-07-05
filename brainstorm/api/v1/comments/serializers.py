import rest_framework.serializers

import comments.models


class CommentSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = comments.models.Comment
        fields = (
            comments.models.Comment.user.field.name,
            comments.models.Comment.text.field.name,
            comments.models.Comment.creation_date.field.name,
            comments.models.Comment.update_date.field.name,
        )
