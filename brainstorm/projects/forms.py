import ckeditor.widgets
import django.core.exceptions
import django.forms
from django.utils.translation import gettext_lazy as _

import core.forms
import projects.models


class ProjectForm(core.forms.BootstrapFormMixin, django.forms.ModelForm):
    preview = django.forms.ImageField(
        label=_('Превью'),
        help_text=_('прикрепите превью проекта'),
        required=False,
    )
    photos = django.forms.ImageField(
        label=_('Фотографии'),
        help_text=_('прикрепите фотки проекта'),
        widget=django.forms.ClearableFileInput(attrs={'multiple': True}),
        required=False,
    )

    class Meta:
        model = projects.models.Project
        fields = (
            projects.models.Project.name.field.name,
            'short_description',
            projects.models.Project.description.field.name,
            projects.models.Project.collaborators.field.name,
            projects.models.Project.status.field.name,
            projects.models.Project.tags.field.name,
        )
        labels = {
            projects.models.Project.name.field.name: _('Название'),
            projects.models.Project.short_description.field.name: _(
                'Краткое описание'
            ),
            projects.models.Project.collaborators.field.name: _(
                'Коллабораторы'
            ),
            projects.models.Project.description.field.name: _('Описание'),
            projects.models.Project.status.field.name: _('Статус'),
            projects.models.Project.tags.field.name: _('Теги'),
        }
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
        tags = self.cleaned_data.get('tags')
        if len(tags) > 5:
            raise django.core.exceptions.ValidationError(_('Максимум 5 тегов'))
