import django.urls

import api.v1.users.views
import api.v1.projects.views

app_name = 'api'
urlpatterns = [
    django.urls.path(
        'userlist/',
        api.v1.users.views.UserList.as_view(),
        name='user_list',
    ),
    django.urls.path(
        'userlist/<int:pk>/',
        api.v1.users.views.UserDetail.as_view(),
        name='user_detail',
    ),
    django.urls.path(
        'projectlist/',
        api.v1.projects.views.ProjectList.as_view(),
        name='project_list',
    ),
    django.urls.path(
        'projectlist/<int:pk>/',
        api.v1.projects.views.ProjectDetail.as_view(),
        name='project_detail',
    )
]
