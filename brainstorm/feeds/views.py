import django.views.generic

# from projects.models import Project


class NewProjectsView(django.views.generic.ListView):
    template_name = 'feeds/feed.html'
    context_object_name = 'projects'
    # queryset = Project.objects.new()


class BestProjectsView(django.views.generic.ListView):
    template_name = 'feeds/feed.html'
    context_object_name = 'projects'
    # queryset = Project.objects.best()


class SpeakedProjectsView(django.views.generic.ListView):
    template_name = 'feeds/feed.html'
    context_object_name = 'projects'
    # queryset = Project.objects.speaked()


class ArchiveProjectsView(django.views.generic.ListView):
    template_name = 'feeds/feed.html'
    context_object_name = 'projects'
    # queryset = Project.objects.archive()
