import django.urls
import django.views.generic

import collaboration.forms
import collaboration.models


class CollaborationRequestFormView(django.views.generic.FormView):
    model = collaboration.models.CollaborationRequest
    form_class = collaboration.forms.CollaboratorRequestForm
    template_name = ''
    success_url = django.urls.reverse_lazy('')


class CollaborationRequestListView(django.views.generic.ListView):
    template_name = ''
    context_object_name = 'requests'
    queryset = collaboration.models.CollaborationRequest.objects.all()
