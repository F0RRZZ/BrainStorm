import django.urls

import api.v1.users.views
import api.v1.projects.views

app_name = 'api'
urlpatterns = [
    django.urls.path(
        'userlist/',
        api.v1.users.views.UserViewSet.as_view({'get': 'list'}),
        name='user_list',
    ),
    django.urls.path(
        'userlist/<int:pk>/',
        api.v1.users.views.UserViewSet.as_view({'get': 'retrieve'}),
        name='user_detail',
    ),
    django.urls.path(
        'projectlist/',
        api.v1.projects.views.ProjectViewSet.as_view({'get': 'list'}),
        name='project_list',
    ),
    django.urls.path(
        'projectlist/<int:pk>/',
        api.v1.projects.views.ProjectViewSet.as_view({'get': 'retrieve'}),
        name='project_detail',
    ),
]
