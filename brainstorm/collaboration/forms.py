import django.forms
from django.utils.translation import gettext_lazy as _

import core.forms
import collaboration.models


class CollaboratorRequestForm(
    core.forms.BootstrapFormMixin, django.forms.ModelForm
):
    class Meta:
        model = collaboration.models.CollaborationRequest
        fields = (
            collaboration.models.CollaborationRequest.contact.field.name,
            collaboration.models.CollaborationRequest.about.field.name,
        )
        labels = {
            collaboration.models.CollaborationRequest.contact.field.name: _(
                'tell_how_to_contact'
            ),
            collaboration.models.CollaborationRequest.about.field.name: _(
                'tell_about_you'
            ),
        }
