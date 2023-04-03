import django.contrib.auth.views
from django.urls import path

from users import views

app_name = 'users'
urlpatterns = [
    path(
        'login/',
        django.contrib.auth.views.LoginView.as_view(
            template_name='registration/login.html',
        ),
        name='login',
    ),
    path(
        'logout/',
        django.contrib.auth.views.LogoutView.as_view(
            template_name='registration/logout.html',
        ),
        name='logout',
    ),
    path(
        'password_change/',
        django.contrib.auth.views.PasswordChangeView.as_view(
            template_name='registration/password_change.html',
        ),
        name='password_change',
    ),
    path(
        'password_change/done',
        django.contrib.auth.views.PasswordChangeDoneView.as_view(
            template_name='registration/password_change_done.html',
        ),
        name='password_change_done',
    ),
    path(
        'password_reset/',
        django.contrib.auth.views.PasswordResetView.as_view(
            template_name='registration/password_reset.html',
        ),
        name='password_reset',
    ),
    path(
        'password_reset/done',
        django.contrib.auth.views.PasswordResetDoneView.as_view(
            template_name='registration/password_reset_done.html',
        ),
        name='password_reset_done',
    ),
    path(
        'reset/<uidb64>/<token>',
        django.contrib.auth.views.PasswordResetConfirmView.as_view(
            template_name='registration/password_reset_confirm.html',
        ),
        name='password_reset_confirm',
    ),
    path(
        'reset/done',
        django.contrib.auth.views.PasswordResetCompleteView.as_view(
            template_name='registration/password_reset_complete.html',
        ),
        name='password_reset_complete',
    ),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path(
        'activate/<str:username>/',
        views.ActivateUserView.as_view(),
        name='activate',
    ),
    path(
        'activate/done',
        views.ActivationDoneView.as_view(),
        name='activation_done',
    ),
]
