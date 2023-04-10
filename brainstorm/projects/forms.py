import django.forms
import projects.models


class ProjectForm(django.forms.ModelForm):
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control mt-2'

    class Meta:
        model = projects.models.Project
        fields = (
            projects.models.Project.name.field.name,
            projects.models.Project.description.field.name,
            projects.models.Project.status.field.name,
        )
        labels = {
            projects.models.Project.name.field.name: 'Название',
            projects.models.Project.description.field.name: 'Описание',
            projects.models.Project.status.field.name: 'Статус',
        }
