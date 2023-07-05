import rest_framework.generics

import api.v1.users.serializers
import users.models


class UserList(rest_framework.generics.ListAPIView):
    queryset = users.models.User.objects.all()
    serializer_class = api.v1.users.serializers.UserSerializer


class UserDetail(rest_framework.generics.RetrieveUpdateDestroyAPIView):
    queryset = users.models.User.objects.all()
    serializer_class = api.v1.users.serializers.UserSerializer
