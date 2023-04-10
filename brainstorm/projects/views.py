import django.contrib.auth.mixins
import django.shortcuts
import django.urls
import django.views.generic
import projects.forms
import projects.models

import users.models


class ViewProject(django.views.generic.TemplateView):
    template_name = 'projects/project_view.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class CreateProject(
    django.contrib.auth.mixins.LoginRequiredMixin,
    django.views.generic.FormView,
):
    template_name = 'projects/project_create.html'
    form_class = projects.forms.ProjectForm
    success_url = django.urls.reverse_lazy('projects:create')

    def form_valid(self, form):
        project = projects.models.Project(
            author=users.models.User.objects.get(pk=self.request.user.id),
            name=form.cleaned_data['name'],
            description=form.cleaned_data['description'],
            status=form.cleaned_data['status'],
        )
        project.save()
        if 'preview' in self.request.FILES:
            image = self.request.FILES.get('preview')
            preview = projects.models.Preview(
                project=project,
                image=image,
            )
            preview.save()
        for image in self.request.FILES.getlist('photos'):
            gallery = projects.models.ImagesGallery(
                project=project,
                image=image,
            )
            gallery.save()
        return super().form_valid(form)


class RedactProject(
    django.contrib.auth.mixins.LoginRequiredMixin,
    django.views.generic.UpdateView,
):
    template_name = 'projects/project_redact.html'
    model = projects.models.Project
    context_object_name = 'project'
    form_class = projects.forms.ProjectForm
    success_url = django.urls.reverse_lazy('core:main')

    def get_object(self, queryset=None):
        return django.shortcuts.get_object_or_404(
            self.model,
            pk=self.kwargs['project_id'],
        )
