import django.shortcuts


def viewprojects(request, project_id):
    template_name = 'projects/project_view.html'
    return django.shortcuts.render(request, template_name)


def createproject(request):
    template_name = 'projects/project_create.html'
    return django.shortcuts.render(request, template_name)


def redactproject(request, project_id):
    template_name = 'projects/project_redact.html'
    return django.shortcuts.render(request, template_name)
