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
        name='request_list',
    ),
    django.urls.path(
        'requests/view/<int:request_id>/',
        collaboration.views.CollaborationRequestDetailView.as_view(template_name='collaboration/request_view.html',),
        name='request_view',
    ),
    django.urls.path(
        'requests/my',
        collaboration.views.UserRequestsListView.as_view(),
        name='my_requests',
    ),
    django.urls.path(
        'requests/my/<int:request_id>/',
        collaboration.views.CollaborationRequestDetailView.as_view(template_name='collaboration/my_request.html',),
        name='my_request',
    ),
]
