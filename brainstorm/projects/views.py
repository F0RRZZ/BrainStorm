import django.http
import django.shortcuts
import django.urls
import django.views.generic

import comments.forms
import projects.models


class ViewProject(
    django.views.generic.DetailView, django.views.generic.FormView
):
    template_name = 'projects/project_view.html'
    pk_url_kwarg = 'project_id'
    model = projects.models.Project
    form_class = comments.forms.CommentForm

    def form_valid(self, form):
        form.save(self.request.user.id, self.get_object().id)
        return django.http.HttpResponseRedirect(
            django.urls.reverse_lazy('projects:view', kwargs=self.kwargs),
        )


class CreateProject(django.views.generic.TemplateView):
    template_name = 'projects/project_create.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class RedactProject(django.views.generic.TemplateView):
    template_name = 'projects/project_redact.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
