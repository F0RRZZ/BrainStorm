import django.db.models
import django.forms
from django.utils.translation import gettext_lazy as _

import collaboration.models


class RequestAnswerForm(django.forms.Form):
    class Status(django.db.models.TextChoices):
        ADOPTED = collaboration.models.CollaborationRequest.Status.ADOPTED
        REJECTED = collaboration.models.CollaborationRequest.Status.REJECTED

    action = django.forms.ChoiceField(
        choices=Status.choices,
        widget=django.forms.RadioSelect(
            attrs={
                "class": "btn-check",
            },
        ),
    )
    answer = django.forms.CharField(
        required=False,
        widget=django.forms.Textarea(
            attrs={
                'rows': 4,
                'placeholder': _('type_message'),
            },
        ),
    )


class CollaboratorRequestForm(django.forms.ModelForm):
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
