import django.urls
import projects.views

app_name = 'projects'

urlpatterns = [
    django.urls.path(
        'view/<int:project_id>',
        projects.views.viewprojects,
        name='create'
    ),
    django.urls.path(
        'create/',
        projects.views.createproject,
        name='create'
    ),
    django.urls.path(
        'redact/<int:project_id>',
        projects.views.redactproject,
        name='create'
    )
]
