import django.contrib.auth.views
import django.urls

import users.views

app_name = 'users'
urlpatterns = [
    django.urls.path(
        'login/',
        users.views.LoginView.as_view(),
        name='login',
    ),
    django.urls.path(
        'logout/',
        django.contrib.auth.views.LogoutView.as_view(),
        name='logout',
    ),
    django.urls.path(
        'password_change/',
        users.views.PasswordChangeView.as_view(),
        name='password_change',
    ),
    django.urls.path(
        'password_change/done/',
        django.contrib.auth.views.PasswordChangeDoneView.as_view(
            template_name='users/password_change_done.html',
        ),
        name='password_change_done',
    ),
    django.urls.path(
        'password_reset/',
        users.views.PasswordResetView.as_view(),
        name='password_reset',
    ),
    django.urls.path(
        'password_reset/done/',
        django.contrib.auth.views.PasswordResetDoneView.as_view(
            template_name='users/password_reset_done.html',
        ),
        name='password_reset_done',
    ),
    django.urls.path(
        'reset/<uidb64>/<token>/',
        django.contrib.auth.views.PasswordResetConfirmView.as_view(
            template_name='users/password_reset_confirm.html',
        ),
        name='password_reset_confirm',
    ),
    django.urls.path(
        'reset/done/',
        django.contrib.auth.views.PasswordResetCompleteView.as_view(
            template_name='users/password_reset_complete.html',
        ),
        name='password_reset_complete',
    ),
    django.urls.path(
        'signup/',
        users.views.SignUpView.as_view(),
        name='signup',
    ),
    django.urls.path(
        'activate/<str:username>/',
        users.views.ActivateUserView.as_view(),
        name='activate',
    ),
    django.urls.path(
        'activate/done',
        users.views.ActivationDoneView.as_view(),
        name='activation_done',
    ),
    django.urls.path(
        'overview/<str:username>/',
        users.views.UserDetailView.as_view(),
        name='overview',
    ),
]
