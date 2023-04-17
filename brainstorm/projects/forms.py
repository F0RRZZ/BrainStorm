import django.forms

import core.forms
import projects.models


class ProjectForm(core.forms.BootstrapFormMixin, django.forms.ModelForm):
    preview = django.forms.ImageField(
        label='Превью',
        help_text='прикрепите превью проекта',
        required=False,
    )
    photos = django.forms.ImageField(
        label='Фотографии',
        help_text='прикрепите фотки проекта',
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
        )
        labels = {
            projects.models.Project.name.field.name: 'Название',
            projects.models.Project.short_description.field.name: (
                'Краткое описание'
            ),
            projects.models.Project.description.field.name: 'Описание',
            projects.models.Project.status.field.name: 'Статус',
        }
