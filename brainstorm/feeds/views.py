from django.utils.translation import gettext_lazy as _
import django.views.generic

import projects.models
import tags.models


class GetContextMixin:
    paginate_by = 30

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = tags.models.Tag.objects.all()
        context['feed_name'] = self.__class__.feed_name
        return context


class NewProjectsView(GetContextMixin, django.views.generic.ListView):
    feed_name = _('new')
    template_name = 'feeds/feed.html'
    context_object_name = 'projects'

    def get_queryset(self):
        tags_slugs = self.request.GET.get('tags', '').split(',')
        if tags_slugs[0]:
            return projects.models.Project.objects.new().filter(
                tags__slug__in=tags_slugs
            )
        return projects.models.Project.objects.new()


class BestProjectsView(GetContextMixin, django.views.generic.ListView):
    feed_name = _('most_popular')
    template_name = 'feeds/feed.html'
    context_object_name = 'projects'
    queryset = projects.models.Project.objects.best()

    def get_queryset(self):
        tags_slugs = self.request.GET.get('tags', '').split(',')
        if tags_slugs[0]:
            return projects.models.Project.objects.best().filter(
                tags__slug__in=tags_slugs
            )
        return projects.models.Project.objects.best()


class SpeakedProjectsView(GetContextMixin, django.views.generic.ListView):
    feed_name = _('most_speaked')
    template_name = 'feeds/feed.html'
    context_object_name = 'projects'
    queryset = projects.models.Project.objects.speaked()

    def get_queryset(self):
        tags_slugs = self.request.GET.get('tags', '').split(',')
        if tags_slugs[0]:
            return projects.models.Project.objects.speaked().filter(
                tags__slug__in=tags_slugs
            )
        return projects.models.Project.objects.speaked()


class ArchiveProjectsView(GetContextMixin, django.views.generic.ListView):
    feed_name = _('projects_archive')
    template_name = 'feeds/feed.html'
    context_object_name = 'projects'
    queryset = projects.models.Project.objects.archive()

    def get_queryset(self):
        tags_slugs = self.request.GET.get('tags', '').split(',')
        if tags_slugs[0]:
            return projects.models.Project.objects.archive().filter(
                tags__slug__in=tags_slugs
            )
        return projects.models.Project.objects.archive()
