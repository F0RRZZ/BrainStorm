import django.urls

import about.views

app_name = 'about'
urlpatterns = [
    django.urls.path(
        '',
        about.views.AboutProjectView.as_view(),
        name='main',
    ),
    django.urls.path(
        'rules/',
        about.views.SiteRulesView.as_view(),
        name='rules',
    ),
]
