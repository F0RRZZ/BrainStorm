import django.urls
from . import views

app_name = 'projects'

urlpatterns = [
    django.urls.path(
        'view/<int:project_id>',
        views.ViewProjects,
        name='create'
    ),
    django.urls.path(
        'create/',
        views.CreateProject,
        name='create'
    ),
    django.urls.path(
        'redact/<int:project_id>',
        views.RedactProject,
        name='create'
    )
]
