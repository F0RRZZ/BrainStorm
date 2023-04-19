import ckeditor.widgets
import django.core.exceptions
import django.forms
from django.utils.translation import gettext_lazy as _

import projects.models


class ProjectForm(django.forms.ModelForm):
    preview = django.forms.ImageField(
        label=_('preview'),
        help_text=_('this_photo_will_be_displayed_as_preview__lowercase'),
        required=False,
    )
    photos = django.forms.ImageField(
        label=_('photos'),
        help_text=_('add_additional_photo_to_project__lowercase'),
        widget=django.forms.ClearableFileInput(attrs={'multiple': True}),
        required=False,
    )

    class Meta:
        model = projects.models.Project
        fields = (
            projects.models.Project.name.field.name,
            projects.models.Project.short_description.field.name,
            projects.models.Project.description.field.name,
            projects.models.Project.status.field.name,
            projects.models.Project.tags.field.name,
        )
        widgets = {
            projects.models.Project.short_description.field.name: (
                ckeditor.widgets.CKEditorWidget()
            ),
            projects.models.Project.description.field.name: (
                ckeditor.widgets.CKEditorWidget()
            ),
        }

    def clean(self):
        super().clean()
        tags = self.cleaned_data.get(projects.models.Project.tags.field.name)
        if len(tags) > 5:
            raise django.core.exceptions.ValidationError(
                _('5_tags_maximum__lowercase').capitalize(),
            )
