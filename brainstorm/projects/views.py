import django.contrib.auth.mixins
import django.core.paginator
import django.http
import django.shortcuts
import django.urls
import django.views.generic

import comments.forms
import comments.models
import projects.forms
import projects.models
import rating.forms
import rating.models
import tags.models
import users.models


class ViewProject(django.views.generic.DetailView):
    template_name = 'projects/project_view.html'
    pk_url_kwarg = 'project_id'
    queryset = projects.models.Project.objects.get_queryset()
    paginate_by = 60

    def get_and_check_initial_rating(self):
        try:
            score = rating.models.ProjectRating.objects.get(
                user_id=self.request.user.id,
                project_id=self.kwargs[self.pk_url_kwarg],
            ).score
            rating_exists = True
        except rating.models.ProjectRating.DoesNotExist:
            score = rating.models.ProjectRating.ScoreData.DEFAULT
            rating_exists = False
        return {
            rating.models.ProjectRating.score.field.name: score
        }, rating_exists

    def get_object(self):
        return django.shortcuts.get_object_or_404(
            projects.models.Project.objects.prefetch_related('tags'),
            id=self.kwargs[self.pk_url_kwarg],
        )

    def get_base_context(self, rating_exists=False):
        project = self.get_object()
        comments_ = comments.models.Comment.objects.get_project_comments(
            project.id,
        )
        paginator = django.core.paginator.Paginator(
            comments_, ViewProject.paginate_by
        )
        page_obj = paginator.get_page(self.request.GET.get('page', 1))
        return {
            'project': project,
            'paginator': paginator,
            'comments': page_obj,
            'average_rating': (
                rating.models.ProjectRating.objects.get_avg_rating(project.id)
            ),
            'rating_exists': rating_exists,
        }

    def get_context_data(self, **kwargs):
        initial_data, rating_exists = self.get_and_check_initial_rating()
        context = self.get_base_context(rating_exists)
        user = self.request.user
        if user.is_authenticated:
            context['comment_form'] = comments.forms.CommentForm()
            context['rating_form'] = rating.forms.ProjectRatingForm(
                initial=initial_data,
            )
        return context

    def post(self, request, project_id):
        initial_data, rating_exists = self.get_and_check_initial_rating()
        context = self.get_base_context(rating_exists)

        user = request.user
        project = context['project']
        comment_form = comments.forms.CommentForm()
        rating_form = rating.forms.ProjectRatingForm(initial_data)

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
                initial=initial_data,
            )
            if rating_form.is_valid():
                rating_form.save(user.id, project.id)
                return django.shortcuts.redirect(
                    django.urls.reverse_lazy(
                        'projects:view', kwargs=self.kwargs
                    ),
                )

        context.update(
            {
                'rating_form': rating_form,
                'comment_form': comment_form,
            }
        )
        return django.shortcuts.render(request, self.template_name, context)


class CreateProject(
    django.contrib.auth.mixins.LoginRequiredMixin,
    django.views.generic.FormView,
):
    template_name = 'projects/project_create.html'
    form_class = projects.forms.ProjectForm
    success_url = django.urls.reverse_lazy('core:main')

    def form_valid(self, form):
        project = projects.models.Project(
            author=users.models.User.objects.get(pk=self.request.user.id),
            name=form.cleaned_data['name'],
            description=form.cleaned_data['description'],
            status=form.cleaned_data['status'],
            short_description=form.cleaned_data['short_description'],
        )
        project.save()
        for tag in form.cleaned_data['tags']:
            project.tags.add(tags.models.Tag.objects.get(name=tag).pk)
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

    def form_valid(self, form):
        project = form.save(commit=False)
        if 'preview' in self.request.FILES:
            preview = projects.models.Preview.objects.filter(
                project=project
            ).first()
            if preview:
                preview.image = self.request.FILES.get('preview')
                preview.save(update_fields=['image'])
            else:
                preview = projects.models.Preview.objects.create(
                    project=project,
                    image=self.request.FILES.get('preview'),
                )
                preview.save()
        photos = self.request.FILES.getlist('photos')
        for photo in photos:
            add_image = projects.models.ImagesGallery.objects.create(
                project=project, image=photo
            )
            add_image.save()
        return super().form_valid(form)


class DeleteProject(django.views.generic.DeleteView):
    pk_url_kwarg = 'project_id'
    model = projects.models.Project
    success_url = django.urls.reverse_lazy('core:main')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        if self.object.author == request.user:
            self.object.delete()
        return django.http.HttpResponseRedirect(success_url)
