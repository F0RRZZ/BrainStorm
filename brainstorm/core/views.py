import django.views.generic


class TestView(django.views.generic.TemplateView):
    def get_template_names(self):
        return [self.kwargs.get('template', 'feeds/feed.html')]
