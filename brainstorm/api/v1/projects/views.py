import rest_framework.viewsets

import api.v1.projects.serializers
import api.v1.projects.permissions
import core.api.permissions
import projects.models


class ProjectViewSet(rest_framework.viewsets.ModelViewSet):
    queryset = projects.models.Project.objects.all()
    serializer_class = api.v1.projects.serializers.ProjectSerializer
    permission_classes = (
        core.api.permissions.IsAdminOrReadOnly,
        api.v1.projects.permissions.IsOwnerOrReadOnly,
    )
