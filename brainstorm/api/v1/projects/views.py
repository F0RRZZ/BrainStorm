import rest_framework.generics
import rest_framework.views

import api.v1.projects.serializers
import projects.models


class ProjectList(rest_framework.generics.ListAPIView):
    queryset = projects.models.Project.objects.all()
    serializer_class = api.v1.projects.serializers.ProjectSerializer


class ProjectDetail(rest_framework.generics.RetrieveUpdateDestroyAPIView):
    queryset = projects.models.Project.objects.all()
    serializer_class = api.v1.projects.serializers.ProjectSerializer
