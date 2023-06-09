from smtplib import SMTPAuthenticationError

import django.conf
import django.contrib.auth.mixins
import django.contrib.auth.views
import django.core.mail
import django.core.paginator
import django.http
import django.shortcuts
import django.urls
import django.utils
import django.views.generic

import comments.models
import projects.models
import users.forms
import users.models


class SignUpView(django.views.generic.CreateView):
    form_class = users.forms.CustomUserCreationForm
    template_name = 'users/signup.html'
    success_url = (
        django.urls.reverse_lazy('users:activation_done')
        if not django.conf.settings.USERS_AUTOACTIVATE
        else django.urls.reverse_lazy('core:main')
    )

    def form_valid(self, form):
        user = form.save(commit=False)
        if not django.conf.settings.USERS_AUTOACTIVATE:
            absolute_url = self.request.build_absolute_uri(
                django.urls.reverse_lazy(
                    'users:activate',
                    args=[user.username],
                )
            )
            try:
                django.core.mail.send_mail(
                    'Подтверждение регистрации',
                    f'Для активации аккаунта'
                    f' перейдите по ссылке: {absolute_url}',
                    django.conf.settings.EMAIL,
                    [user.email],
                    fail_silently=False,
                )
                user.is_active = False
                user.save()
            except SMTPAuthenticationError:
                user.is_active = True
                user.save()
                return django.shortcuts.redirect('core:main')
        else:
            user.is_active = True
            user.save()
        return super().form_valid(form)


class ActivateUserView(django.views.generic.DetailView):
    model = users.models.User
    template_name = 'users/confirm_email.html'

    def get_object(self, queryset=None):
        user = django.shortcuts.get_object_or_404(
            users.models.User, username=self.kwargs['username']
        )

        if user.last_login is None:
            if (
                django.utils.timezone.now() - user.date_joined
                > django.utils.timezone.timedelta(hours=12)
            ):
                raise django.http.Http404
        else:
            if (
                django.utils.timezone.now() - user.date_joined
                > django.utils.timezone.timedelta(weeks=1)
            ):
                raise django.http.Http404

        user.is_active = True
        user.save()

        return user


class UserDetailView(
    django.views.generic.UpdateView,
):
    template_name = 'users/user_detail.html'
    pk_url_kwarg = 'username'
    paginate_by = 6

    queryset = users.models.User.objects.user_profile()
    form_class = users.forms.UserProfileForm

    context_object_name = 'rendering_user'

    def get_success_url(self):
        return self.request.path

    def form_valid(self, form):
        super().form_valid(form)
        return django.http.HttpResponseRedirect(
            django.urls.reverse_lazy(
                'users:overview',
                kwargs={
                    self.pk_url_kwarg: form.cleaned_data[
                        users.models.User.username.field.name
                    ],
                },
            ),
        )

    def get_object(self):
        return django.shortcuts.get_object_or_404(
            self.queryset,
            username=self.kwargs[self.pk_url_kwarg],
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.object
        current_user = self.request.user
        show_profile = (
            current_user.is_authenticated and current_user.id == user.id
        )

        projects_ = projects.models.Project.objects.get_for_user_detail(
            user.id,
        )
        projects_paginator = django.core.paginator.Paginator(
            projects_,
            UserDetailView.paginate_by,
        )
        projects_page_obj = projects_paginator.get_page(
            self.request.GET.get('projects_page', 1),
        )

        comments_ = comments.models.Comment.objects.get_for_user_detail(
            user.id,
        )
        comments_paginator = django.core.paginator.Paginator(
            comments_,
            UserDetailView.paginate_by,
        )
        comments_page_obj = comments_paginator.get_page(
            self.request.GET.get('comments_page', 1),
        )
        projects_objects = projects.models.Project.objects
        collab = projects_objects.get_for_user_detail_by_collaborator(user.id)
        collaboration_paginator = django.core.paginator.Paginator(
            collab,
            UserDetailView.paginate_by,
        )
        collaboration_page_obj = collaboration_paginator.get_page(
            self.request.GET.get('collaboration_page', 1),
        )

        context.update(
            {
                'projects_paginator': projects_paginator,
                'projects': projects_page_obj,
                'comments_paginator': comments_paginator,
                'comments': comments_page_obj,
                'collaboration_paginator': collaboration_paginator,
                'collaboration': collaboration_page_obj,
                'show_profile': show_profile,
            }
        )
        return context


class ActivationDoneView(
    django.views.generic.TemplateView,
    django.contrib.auth.mixins.LoginRequiredMixin,
):
    template_name = 'users/activate_link_sends.html'
