import rest_framework.serializers

import tags.models


class TagSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = tags.models.Tag
        fields = (
            tags.models.Tag.name.field.name,
            tags.models.Tag.description.field.name,
        )
