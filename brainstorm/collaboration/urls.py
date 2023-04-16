import django.urls

import collaboration.views

app_name = 'collaboration'
urlpatterns = [
    django.urls.path(
        'request/<int:project_id>/',
        collaboration.views.CollaborationRequestFormView.as_view(),
        name='request',
    ),
    django.urls.path(
        'list/<int:project_id>/',
        collaboration.views.CollaborationRequestListView.as_view(),
        name='list',
    ),
]
