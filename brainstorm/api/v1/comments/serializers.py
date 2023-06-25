import rest_framework.serializers

import api.v1.users.serializers
import comments.models


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
