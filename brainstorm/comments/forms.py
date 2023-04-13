import comments.models
import django.forms
from django.utils.translation import gettext_lazy as _

import core.forms


class CommentForm(core.forms.BootstrapFormMixin, django.forms.ModelForm):
    def save(self, user_id, project_id, commit=True):
        comment = super().save(commit=False)
        comment.user_id = user_id
        comment.project_id = project_id
        if commit:
            comment.save()
        return comment

    class Meta:
        model = comments.models.Comment

        fields = [
            comments.models.Comment.text.field.name,
        ]
        placeholders = {
            comments.models.Comment.text.field.name: _('type_text'),
        }
        widgets = {
            comments.models.Comment.text.field.name: django.forms.Textarea(
                attrs={'rows': 2},
            ),
        }
