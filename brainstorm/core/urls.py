import django.urls

import core.views

app_name = 'core'
urlpatterns = [
    django.urls.path(
        '',
        core.views.TestView.as_view(),
        name='main',
    ),
]
