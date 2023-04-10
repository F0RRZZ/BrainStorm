import django.urls

import feeds.views

app_name = 'core'
urlpatterns = [
    django.urls.path(
        '',
        feeds.views.NewProjectsView.as_view(),
        name='main',
    ),
]
