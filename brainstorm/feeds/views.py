import django.views.generic
import projects.models


class NewProjectsView(django.views.generic.ListView):
    template_name = 'feeds/feed.html'
    context_object_name = 'projects'
    queryset = projects.models.Project.objects.new()


class BestProjectsView(django.views.generic.ListView):
    template_name = 'feeds/feed.html'
    context_object_name = 'projects'
    queryset = projects.models.Project.objects.best()


class SpeakedProjectsView(django.views.generic.ListView):
    template_name = 'feeds/feed.html'
    context_object_name = 'projects'
    # queryset = Project.objects.speaked()


class ArchiveProjectsView(django.views.generic.ListView):
    template_name = 'feeds/feed.html'
    context_object_name = 'projects'
    queryset = projects.models.Project.objects.archive()
