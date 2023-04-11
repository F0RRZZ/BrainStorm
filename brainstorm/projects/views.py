import django.contrib.auth.mixins
import django.http
import django.shortcuts
import django.urls
import django.views.generic

import comments.forms
import projects.forms
import projects.models
import rating.forms
import rating.models
import users.models


class ViewProject(django.views.generic.DetailView):
    template_name = 'projects/project_view.html'
    pk_url_kwarg = 'project_id'
    model = projects.models.Project

    # def form_valid(self, form):
    #     form.save(self.request.user.id, self.get_object().id)
    #     return django.http.HttpResponseRedirect(
    #         django.urls.reverse_lazy('projects:view', kwargs=self.kwargs),
    #     )

    def get_initial_rating(self):
        try:
            score = rating.models.ProjectRating.objects.get(
                user_id=self.request.user.id,
                project_id=self.kwargs[self.pk_url_kwarg],
            ).score
        except rating.models.ProjectRating.DoesNotExist:
            score = rating.models.ProjectRating.ScoreData.DEFAULT
        return {rating.models.ProjectRating.score.field.name: score}

    def get_object(self):
        return django.shortcuts.get_object_or_404(
            projects.models.Project,
            id=self.kwargs[self.pk_url_kwarg],
        )

    def get_context_data(self, **kwargs):
        context = {
            'project': self.get_object(),
        }
        user = self.request.user
        if user.is_authenticated:
            context['comment_form'] = comments.forms.CommentForm()
            context['rating_form'] = rating.forms.ProjectRatingForm(
                initial=self.get_initial_rating(),
            )
        return context

    def post(self, request, project_id):
        user = request.user
        project = self.get_object()
        comment_form = comments.forms.CommentForm()
        rating_form = rating.forms.ProjectRatingForm()

        action = self.request.POST['action']

        if action == 'leave_comment':
            comment_form = comments.forms.CommentForm(request.POST or None)
            if comment_form.is_valid():
                comment_form.save(user.id, project.id)
                return django.shortcuts.redirect(
                    django.urls.reverse_lazy(
                        'projects:view', kwargs=self.kwargs
                    ),
                )
        elif action == 'set_rating':
            rating_form = rating.forms.ProjectRatingForm(
                request.POST or None,
                initial=self.get_initial_rating(),
            )
            if rating_form.is_valid():
                rating_form.save(user.id, project.id)
                return django.shortcuts.redirect(
                    django.urls.reverse_lazy(
                        'projects:view', kwargs=self.kwargs
                    ),
                )

        context = {
            'project': project,
            'rating_form': rating_form,
            'comment_form': comment_form,
        }
        return django.shortcuts.render(request, self.template_name, context)


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
