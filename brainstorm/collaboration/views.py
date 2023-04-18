import django.contrib.auth.mixins
import django.http
import django.shortcuts
import django.urls
import django.views.generic

import collaboration.forms
import collaboration.models
import projects.models


class AddProjectToContextMixin:
    def dispatch(self, request, *args, **kwargs):
        self.project = django.shortcuts.get_object_or_404(
            projects.models.Project.objects.only(
                projects.models.Project.name.field.name,
                projects.models.Project.author_id.field.name,
            ),
            id=self.kwargs[self.pk_url_kwarg],
        )
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.project
        return context


class RequestCreateView(
    AddProjectToContextMixin,
    django.views.generic.FormView,
    django.contrib.auth.mixins.LoginRequiredMixin,
):
    model = collaboration.models.CollaborationRequest
    form_class = collaboration.forms.CollaboratorRequestForm
    template_name = 'collaboration/request_create.html'
    pk_url_kwarg = 'project_id'

    def dispatch(self, request, *args, **kwargs):
        result = super().dispatch(request, *args, **kwargs)
        user = self.request.user
        if user.id == self.project.author_id:
            raise django.http.Http404()
        collaborators_id = self.project.collaborators.values_list(
            projects.models.Project.id.field.name,
            flat=True,
        )
        if user.id in collaborators_id:
            raise django.http.Http404()
        return result

    def form_valid(self, form):
        self.request_id = form.save(
            self.request.user.id, self.kwargs[self.pk_url_kwarg]
        ).id
        return super().form_valid(form)

    def get_success_url(self):
        return django.urls.reverse_lazy(
            'collaboration:my_request',
            kwargs={
                'request_id': self.request_id,
            },
        )


class RequestsListView(
    AddProjectToContextMixin,
    django.views.generic.ListView,
    django.contrib.auth.mixins.LoginRequiredMixin,
):
    template_name = 'collaboration/request_list.html'
    context_object_name = 'requests'
    pk_url_kwarg = 'project_id'

    def dispatch(self, request, *args, **kwargs):
        result = super().dispatch(request, *args, **kwargs)
        user = self.request.user
        if user.id != self.project.author_id:
            raise django.http.Http404()
        return result

    def get_queryset(self):
        return collaboration.models.CollaborationRequest.objects.get_for_list(
            self.kwargs[self.pk_url_kwarg],
        )


class MyRequestsListView(
    django.views.generic.ListView,
    django.contrib.auth.mixins.LoginRequiredMixin,
):
    template_name = 'collaboration/my_request_list.html'
    context_object_name = 'requests'

    def get_queryset(self):
        return (
            collaboration.models.CollaborationRequest.objects.get_for_my_list(
                self.request.user.id,
            )
        )


class MyRequestDetailView(
    django.views.generic.DetailView,
    django.contrib.auth.mixins.LoginRequiredMixin,
):
    template_name = 'collaboration/my_request_detail.html'
    context_object_name = 'request'
    pk_url_kwarg = 'request_id'

    def get_queryset(self):
        model = collaboration.models.CollaborationRequest
        return model.objects.get_for_my_detail()

    def get_object(self, queryset=None):
        object_ = super().get_object(queryset)
        if object_.user_id != self.request.user.id:
            raise django.http.Http404()
        return object_


class RequestDetailView(
    django.views.generic.DetailView,
    django.views.generic.FormView,
    django.contrib.auth.mixins.LoginRequiredMixin,
):
    template_name = 'collaboration/request_detail.html'
    form_class = collaboration.forms.RequestAnswerForm
    context_object_name = 'request'
    pk_url_kwarg = 'request_id'

    def get_queryset(self):
        return (
            collaboration.models.CollaborationRequest.objects.get_for_detail()
        )

    def get_success_url(self):
        return self.request.path

    def form_valid(self, form):
        collab_request = self.get_object()
        collab_request.answer = form.cleaned_data['answer']
        action = form.cleaned_data['action']
        if action == collaboration.forms.RequestAnswerForm.Status.ADOPT:
            collab_request.status = (
                collaboration.models.CollaborationRequest.Status.ADOPTED
            )
            collab_request.project.collaborators.add(collab_request.user)
        if action == collaboration.forms.RequestAnswerForm.Status.REJECT:
            collab_request.status = (
                collaboration.models.CollaborationRequest.Status.REJECTED
            )
        collab_request.save()
        return super().form_valid(form)

    def get_object(self, queryset=None):
        object_ = super().get_object(queryset)
        if object_.project.author_id != self.request.user.id:
            raise django.http.Http404()
        return object_
