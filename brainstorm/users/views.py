from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, DetailView, UpdateView
from users.forms import CustomUserCreationForm, UserProfileForm
from users.models import User


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


class ActivateUserView(DetailView):
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


class UserDetailView(DetailView):
    # TODO: add projects and comments in context

    template_name = 'users/user_detail.html'
    queryset = User.objects.all()
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


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image'] = self.request.user.image
        return context
