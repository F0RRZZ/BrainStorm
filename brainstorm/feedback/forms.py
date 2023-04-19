import django.forms
from django.utils.translation import gettext_lazy as _

import core.forms
import feedback.models


class FeedbackForm(core.forms.BootstrapFormMixin, django.forms.ModelForm):
    email = django.forms.EmailField(
        widget=django.forms.EmailInput(
            attrs={'placeholder': 'example@example.com'},
        ),
        label=feedback.models.PersonalData.email.field.verbose_name,
        help_text=feedback.models.PersonalData.email.field.help_text,
    )
    files = django.forms.FileField(
        widget=django.forms.ClearableFileInput(attrs={'multiple': True}),
        required=False,
        label=_('files'),
        help_text=_('add_some_files_if_necessary__lowercase'),
    )

    class Meta:
        model = feedback.models.Feedback
        fields = (
            feedback.models.Feedback.subject.field.name,
            feedback.models.Feedback.text.field.name,
        )
        widget = {
            feedback.models.Feedback.text.field.name: django.forms.Textarea(
                attrs={'rows': 5},
            ),
        }
