import django.urls

import api.v1.users.routers
import api.v1.projects.routers

app_name = 'api'
urlpatterns = [
    django.urls.path(
        '', django.urls.include(api.v1.users.routers.router.urls)
    ),
    django.urls.path(
        '', django.urls.include(api.v1.projects.routers.router.urls)
    ),
]
