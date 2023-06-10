import rest_framework.serializers

import users.models


class UserSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = users.models.User
        fields = (
            users.models.User.first_name.field.name,
            users.models.User.last_name.field.name,
            users.models.User.username.field.name,
            users.models.User.bio.field.name,
            users.models.User.email.field.name,
            users.models.User.date_joined.field.name,
        )
