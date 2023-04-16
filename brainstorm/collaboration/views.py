import django.contrib.auth.mixins
import django.shortcuts
import django.urls
import django.views.generic

import collaboration.forms
import collaboration.models
import projects.models


class AddProjectToContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = django.shortcuts.get_object_or_404(
            projects.models.Project.objects.only(
                projects.models.Project.name.field.name
            ),
            id=self.kwargs[self.pk_url_kwarg],
        )
        return context


class CollaborationRequestFormView(
    AddProjectToContextMixin,
    django.views.generic.FormView,
    django.contrib.auth.mixins.LoginRequiredMixin,
):
    model = collaboration.models.CollaborationRequest
    form_class = collaboration.forms.CollaboratorRequestForm
    template_name = 'collaboration/request_create.html'
    pk_url_kwarg = 'project_id'

    def form_valid(self, form):
        form.save(self.request.user.id, self.kwargs[self.pk_url_kwarg])
        return super().form_valid(form)

    def get_success_url(self):
        return django.urls.reverse_lazy('projects:view', kwargs=self.kwargs)


class CollaborationRequestListView(
    AddProjectToContextMixin,
    django.views.generic.ListView,
    django.contrib.auth.mixins.LoginRequiredMixin,
):
    template_name = 'collaboration/request_list.html'
    context_object_name = 'requests'
    pk_url_kwarg = 'project_id'

    def get_queryset(self):
        return (
            collaboration.models.CollaborationRequest.objects.get_for_project(
                self.kwargs[self.pk_url_kwarg],
            )
        )


class UserRequestsListView(
    django.views.generic.ListView,
    django.contrib.auth.mixins.LoginRequiredMixin,
):
    template_name = 'collaboration/my_requests.html'
    context_object_name = 'requests'

    def get_queryset(self):
        return collaboration.models.CollaborationRequest.objects.get_for_user(
            self.request.user.id,
        )


class CollaborationRequestDetailView(
    django.views.generic.DetailView,
    django.contrib.auth.mixins.LoginRequiredMixin,
):
    template_name = 'collaboration/request_view.html'
    context_object_name = 'request'
    pk_url_kwarg = 'request_id'

    queryset = collaboration.models.CollaborationRequest.objects.all()
