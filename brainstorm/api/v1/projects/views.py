import rest_framework.viewsets

import api.v1.projects.serializers
import projects.models


class ProjectViewSet(rest_framework.viewsets.ModelViewSet):
    queryset = projects.models.Project.objects.all()
    serializer_class = api.v1.projects.serializers.ProjectSerializer
