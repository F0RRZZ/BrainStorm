import django.urls

import collaboration.views

app_name = 'collaboration'
urlpatterns = [
    django.urls.path(
        'requests/create/<int:project_id>/',
        collaboration.views.CollaborationRequestFormView.as_view(),
        name='create_request',
    ),
    django.urls.path(
        'list/<int:project_id>/',
        collaboration.views.CollaborationRequestListView.as_view(),
        name='list',
    ),
    django.urls.path(
        'requests/view/<int:request_id>/',
        collaboration.views.CollaborationRequestListView.as_view(),
        name='list',
    ),
]
