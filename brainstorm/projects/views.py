import django.shortcuts


def ViewProjects(request, project_id):
    template_name = 'projects/project_view.html'
    return django.shortcuts.render(request, template_name)


def CreateProject(request):
    template_name = 'projects/project_create.html'
    return django.shortcuts.render(request, template_name)


def RedactProject(request, project_id):
    template_name = 'projects/project_redact.html'
    return django.shortcuts.render(request, template_name)
