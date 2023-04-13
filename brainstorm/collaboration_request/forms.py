import django.forms

import core.forms
import collaboration_request.models as collab_models


class CollaboratorRequestForm(
    core.forms.BootstrapFormMixin, django.forms.ModelForm
):
    class Meta:
        model = collab_models.CollaborationRequest
        fields = (
            collab_models.CollaborationRequest.subject.field.name,
            collab_models.CollaborationRequest.text.field.name,
        )
        labels = {
            collab_models.CollaborationRequest.subject.field.name: 'Тема',
            collab_models.CollaborationRequest.text.field.name: 'Текст',
        }
