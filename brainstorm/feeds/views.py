import django.db.models
from django.utils.translation import gettext_lazy as _
import django.views.generic

import projects.models
import tags.models


class GetContextMixin:
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = tags.models.Tag.objects.all()
        context['feed_name'] = self.__class__.feed_name
        return context

    def get_queryset(self):
        search = self.request.GET.get('search', '')
        tags_slugs = self.request.GET.get('tags', '').split(',')
        obj = self.queryset.filter(
            django.db.models.Q(name__icontains=search)
            | django.db.models.Q(short_description__icontains=search)
            | django.db.models.Q(description__icontains=search),
        )
        if tags_slugs[0]:
            for tag in tags_slugs:
                obj = obj.filter(tags__slug=tag)
        return obj.distinct()


class NewProjectsView(GetContextMixin, django.views.generic.ListView):
    feed_name = _('new')
    template_name = 'feeds/feed.html'
    context_object_name = 'projects'
    queryset = projects.models.Project.objects.new()


class BestProjectsView(GetContextMixin, django.views.generic.ListView):
    feed_name = _('most_popular')
    template_name = 'feeds/feed.html'
    context_object_name = 'projects'
    queryset = projects.models.Project.objects.best()


class SpeakedProjectsView(GetContextMixin, django.views.generic.ListView):
    feed_name = _('most_speaked')
    template_name = 'feeds/feed.html'
    context_object_name = 'projects'
    queryset = projects.models.Project.objects.speaked()


class ArchiveProjectsView(GetContextMixin, django.views.generic.ListView):
    feed_name = _('projects_archive')
    template_name = 'feeds/feed.html'
    context_object_name = 'projects'
    queryset = projects.models.Project.objects.archive()
