import django.contrib.auth.mixins
import django.http
import django.shortcuts
import django.urls
import django.views.generic

import comments.forms
import projects.forms
import projects.models
import users.models


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
