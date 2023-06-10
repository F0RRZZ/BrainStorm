import django.urls

import api.v1.users.views

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
]
