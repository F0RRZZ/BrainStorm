import rest_framework.viewsets

import api.v1.users.serializers
import users.models


class UserViewSet(rest_framework.viewsets.ModelViewSet):
    queryset = users.models.User.objects.all()
    serializer_class = api.v1.users.serializers.UserSerializer
