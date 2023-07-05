import rest_framework.serializers

import api.v1.comments.serializers
import users.models


class UserSerializer(rest_framework.serializers.ModelSerializer):
    comments = api.v1.comments.serializers.CommentSerializer(
        many=True, read_only=True
    )

    class Meta:
        model = users.models.User
        fields = (
            users.models.User.first_name.field.name,
            users.models.User.last_name.field.name,
            users.models.User.username.field.name,
            users.models.User.bio.field.name,
            users.models.User.email.field.name,
            users.models.User.date_joined.field.name,
            'comments',
        )
