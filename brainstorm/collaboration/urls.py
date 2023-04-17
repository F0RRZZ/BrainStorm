import django.urls

import collaboration.views

app_name = 'collaboration'
urlpatterns = [
    django.urls.path(
        'requests/create/<int:project_id>/',
        collaboration.views.RequestCreateView.as_view(),
        name='create_request',
    ),
    django.urls.path(
        'list/<int:project_id>/',
        collaboration.views.RequestsListView.as_view(),
        name='request_list',
    ),
    django.urls.path(
        'requests/view/<int:request_id>/',
        collaboration.views.RequestDetailView.as_view(),
        name='request_view',
    ),
    django.urls.path(
        'requests/my',
        collaboration.views.MyRequestDetailView.as_view(),
        name='my_requests',
    ),
    django.urls.path(
        'requests/my/<int:request_id>/',
        collaboration.views.MyRequestsListView.as_view(),
        name='my_request',
    ),
]
