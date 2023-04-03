from django.conf import settings
from django.core.mail import send_mail
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, DetailView

from users.models import User
from users.forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/signup.html'
    success_url = (
        reverse_lazy('users:activation_done')
        if not settings.DEBUG
        else reverse_lazy('index:index')
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


class ActivateUser(DetailView):
    model = User
    template_name = 'users/confirm_email.html'

    def get_object(self, queryset=None):
        user = get_object_or_404(User, username=self.kwargs['username'])

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
