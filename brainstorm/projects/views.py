import django.shortcuts
import django.views.generic


class ViewProject(django.views.generic.TemplateView):
    template_name = 'projects/project_view.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class CreateProject(django.views.generic.TemplateView):
    template_name = 'projects/project_create.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class RedactProject(django.views.generic.TemplateView):
    template_name = 'projects/project_redact.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
