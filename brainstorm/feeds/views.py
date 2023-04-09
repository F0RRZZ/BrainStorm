import django.views.generic

import projects.models
import tags.models


class GetContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = tags.models.Tag.objects.all()
        context['feed_name'] = self.__class__.feed_name
        return context


class NewProjectsView(GetContextMixin, django.views.generic.ListView):
    feed_name = 'Последние активные'
    template_name = 'feeds/feed.html'
    context_object_name = 'projects'
    queryset = projects.models.Project.objects.all()


class BestProjectsView(GetContextMixin, django.views.generic.ListView):
    feed_name = 'Самые популярные'
    template_name = 'feeds/feed.html'
    context_object_name = 'projects'
    queryset = projects.models.Project.objects.all()


class SpeakedProjectsView(GetContextMixin, django.views.generic.ListView):
    feed_name = 'Самые обсуждаемые'
    template_name = 'feeds/feed.html'
    context_object_name = 'projects'
    queryset = projects.models.Project.objects.all()


class ArchiveProjectsView(GetContextMixin, django.views.generic.ListView):
    feed_name = 'Архив проектов'
    template_name = 'feeds/feed.html'
    context_object_name = 'projects'
    queryset = projects.models.Project.objects.all()
