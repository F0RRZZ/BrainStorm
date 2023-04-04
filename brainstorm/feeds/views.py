from django.views.generic import ListView
from projects.models import Project


class NewProjectsView(ListView):
    template_name = 'feeds/new_projects_feed.html'
    context_object_name = 'projects'
    queryset = Project.objects.new()


class BestProjectsView(ListView):
    template_name = 'feeds/best_projects_feed.html'
    context_object_name = 'projects'
    queryset = Project.objects.best()


class SpeakedProjectsView(ListView):
    template_name = 'feeds/speaked_projects_feed.html'
    context_object_name = 'projects'
    queryset = Project.objects.speaked()


class ArchiveProjectsView(ListView):
    template_name = 'feeds/archive_projects_feed.html'
    context_object_name = 'projects'
    queryset = Project.objects.archive()
