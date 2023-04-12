import django.views.generic

import collaboration_request.forms
import collaboration_request.models


class CollaborationRequestFormView(django.views.generic.FormView):
    model = collaboration_request.models.CollaborationRequest
    form_class = collaboration_request.forms.CollaborationRequestForm
    template_name = ''
    success_url = django.urls.reversed_lazy('')


class CollaborationRequestListView(django.views.generic.ListView):
    template_name = ''
    context_object_name = 'requests'
    queryset = collaboration_request.models.CollaborationRequest.objects.all()
