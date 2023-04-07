import django.views.generic


class AboutProjectView(django.views.generic.TemplateView):
    template_name = 'about/main.html'


class SiteRulesView(django.views.generic.TemplateView):
    template_name = 'about/rules.html'
