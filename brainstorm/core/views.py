import django.views.generic

import tags.models


class TestView(django.views.generic.TemplateView):
    template_name = 'feeds/feed.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = tags.models.Tag.objects.all()
        return context
