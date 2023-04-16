import django.forms
from django.utils.translation import gettext_lazy as _

import collaboration.models
import core.forms


class CollaboratorRequestForm(
    core.forms.BootstrapFormMixin, django.forms.ModelForm
):
    def save(self, user_id, project_id, commit=True):
        request = super().save(commit=False)
        request.user_id = user_id
        request.project_id = project_id
        request.save()
        return request

    class Meta:
        model = collaboration.models.CollaborationRequest
        fields = (
            collaboration.models.CollaborationRequest.contact.field.name,
            collaboration.models.CollaborationRequest.about.field.name,
        )
        widgets = {
            collaboration.models.CollaborationRequest.contact.field.name: (
                django.forms.Textarea(
                    attrs={
                        'rows': 3,
                    },
                )
            ),
        }
        labels = {
            collaboration.models.CollaborationRequest.contact.field.name: _(
                'tell_how_to_contact'
            ),
            collaboration.models.CollaborationRequest.about.field.name: _(
                'tell_about_you'
            ),
        }
