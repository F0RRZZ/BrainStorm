import django.urls

import projects.views

app_name = 'projects'

urlpatterns = [
    django.urls.path(
        'view/<int:project_id>',
        projects.views.ViewProject.as_view(),
        name='view',
    ),
    django.urls.path(
        'create/',
        projects.views.CreateProject.as_view(),
        name='create',
    ),
    django.urls.path(
        'redact/<int:project_id>',
        projects.views.RedactProject.as_view(),
        name='redact',
    ),
    django.urls.path(
        'delete/<int:project_id>',
        projects.views.DeleteProject.as_view(),
        name='delete',
    ),
]
