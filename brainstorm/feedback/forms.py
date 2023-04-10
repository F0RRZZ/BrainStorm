import django.forms

import core.forms
import feedback.models


class FeedbackForm(core.forms.BootstrapFormMixin, django.forms.ModelForm):
    email = django.forms.EmailField(
        widget=django.forms.EmailInput(
            attrs={'placeholder': 'example@example.com'},
        ),
        label='Почта',
        help_text='введите свою почту',
    )
    files = django.forms.FileField(
        widget=django.forms.ClearableFileInput(attrs={'multiple': True}),
        required=False,
        label='Файлы',
        help_text='Приложите файлы',
    )

    class Meta:
        model = feedback.models.Feedback
        fields = (
            feedback.models.Feedback.subject.field.name,
            feedback.models.Feedback.text.field.name,
        )
        labels = {
            feedback.models.Feedback.subject.field.name: 'Тема',
            feedback.models.Feedback.text.field.name: 'Текст',
        }
        widget = {
            feedback.models.Feedback.text.field.name: django.forms.Textarea(
                attrs={'rows': 5},
            ),
        }
