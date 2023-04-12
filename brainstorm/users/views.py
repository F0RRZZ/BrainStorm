import django.conf
import django.contrib.auth.mixins
import django.contrib.auth.views
import django.core.mail
import django.http
import django.shortcuts
import django.urls
import django.utils
import django.views.generic

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
            user.is_activate = False
            user.save()

            absolute_url = self.request.build_absolute_uri(
                django.urls.reverse_lazy(
                    'users:activate',
                    args=[user.username],
                )
            )

            django.core.mail.send_mail(
                'Подтверждение регистрации',
                f'Для активации аккаунта перейдите по ссылке: {absolute_url}',
                django.conf.settings.EMAIL,
                [user.email],
                fail_silently=False,
            )
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
    django.views.generic.DetailView,
):
    template_name = 'users/user_detail.html'
    pk_url_kwarg = 'username'

    model = users.models.User
    form_class = users.forms.UserProfileForm

    context_object_name = 'rendering_user'

    def get_success_url(self):
        return django.urls.reverse_lazy('users:overview', kwargs=self.kwargs)

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
            self.get_queryset().select_related(),
            username=self.kwargs[self.pk_url_kwarg],
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.object
        current_user = self.request.user
        first_name = user.first_name
        last_name = user.last_name
        image = user.image
        show_profile = (
            current_user.is_authenticated and current_user.id == user.id
        )
        context.update(
            {
                'first_name': first_name
                if first_name is not None
                else 'не указано',
                'last_name': last_name
                if last_name is not None
                else 'не указано',
                'image': image if last_name is not None else 'не указано',
                'show_profile': show_profile,
            }
        )
        return context


class ActivationDoneView(
    django.views.generic.TemplateView,
    django.contrib.auth.mixins.LoginRequiredMixin,
):
    template_name = 'users/activate_link_sends.html'


class LoginView(
    django.contrib.auth.views.LoginView,
):
    form_class = users.forms.LoginForm
    template_name = 'users/login.html'


class PasswordChangeView(
    django.contrib.auth.views.PasswordChangeView,
):
    form_class = users.forms.PasswordChangeForm
    template_name = 'users/password_change.html'


class PasswordResetView(
    django.contrib.auth.views.PasswordResetView,
):
    form_class = users.forms.PasswordResetForm
    template_name = 'users/password_reset.html'
