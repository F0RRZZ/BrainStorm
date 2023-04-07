from django import forms

from core.forms import BootstrapFormMixin
from feedback.models import Feedback


class FeedbackForm(BootstrapFormMixin, forms.ModelForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'example@example.com'},
        ),
        label='Почта',
        help_text='введите свою почту',
    )
    files = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
        required=False,
        label='Файлы',
        help_text='Приложите файлы',
    )

    class Meta:
        model = Feedback
        fields = (
            Feedback.subject.field.name,
            Feedback.text.field.name,
        )
        labels = {
            Feedback.subject.field.name: 'Тема',
            Feedback.text.field.name: 'Текст',
        }
        widget = {
            Feedback.text.field.name: forms.Textarea(
                attrs={'rows': 5},
            ),
        }
