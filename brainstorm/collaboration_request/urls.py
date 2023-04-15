import collaboration_request.views as collab_views
import django.urls

app_name = 'collaboration_requests'
urlpatterns = [
    django.urls.path(
        'request/',
        collab_views.CollaborationRequestFormView.as_view(),
        name='request',
    ),
    django.urls.path(
        'list/',
        collab_views.CollaborationRequestListView.as_view(),
        name='list',
    ),
]
