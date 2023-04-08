from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
import django.contrib.auth.views
from django.core.mail import send_mail
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
import django.views.generic

import users.forms
import users.models


class SignUpView(django.views.generic.CreateView):
    form_class = users.forms.CustomUserCreationForm
    template_name = 'users/signup.html'
    success_url = (
        reverse_lazy('users:activation_done')
        if not settings.DEBUG
        else reverse_lazy('core:main')
    )

    def form_valid(self, form):
        user = form.save(commit=False)
        if not settings.USERS_AUTOACTIVATE:
            user.is_activate = False
            user.save()

            absolute_url = self.request.build_absolute_uri(
                reverse_lazy(
                    'users:activate',
                    args=[user.username],
                )
            )

            send_mail(
                'Подтверждение регистрации',
                f'Для активации аккаунта перейдите по ссылке: {absolute_url}',
                settings.EMAIL,
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
        user = get_object_or_404(
            users.models.User, username=self.kwargs['username']
        )

        if user.last_login is None:
            if timezone.now() - user.date_joined > timezone.timedelta(
                hours=12
            ):
                raise Http404
        else:
            if timezone.now() - user.date_joined > timezone.timedelta(weeks=1):
                raise Http404

        user.is_active = True
        user.save()

        return user


class UserDetailView(django.views.generic.DetailView):
    # TODO: add projects and comments in context

    template_name = 'users/user_detail.html'
    queryset = users.models.User.objects.all()
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.object
        first_name = user.first_name if user.first_name else 'не указано'
        last_name = user.last_name if user.last_name else 'не указано'
        image = user.image if user.image else 'не указано'
        projects = None
        comments = None
        context.update(
            {
                'first_name': first_name,
                'last_name': last_name,
                'image': image,
                'projects': projects,
                'comments': comments,
            }
        )
        return context


class ActivationDoneView(
    django.views.generic.TemplateView, LoginRequiredMixin
):
    template_name = 'users/activate_link_sends.html'


class ProfileView(LoginRequiredMixin, django.views.generic.UpdateView):
    model = users.models.User
    form_class = users.forms.UserProfileForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image'] = self.request.user.image
        return context


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
