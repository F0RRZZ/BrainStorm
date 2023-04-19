import django.forms
import django.forms.widgets

import rating.models


class RangeInput(django.forms.TextInput):
    input_type = 'range'


class ProjectRatingForm(django.forms.ModelForm):
    def save(self, user_id, project_id, commit=True):
        rating_ = super().save(commit=False)
        try:
            existed = rating.models.ProjectRating.objects.get(
                user_id=user_id,
                project_id=project_id,
            )
        except rating.models.ProjectRating.DoesNotExist:
            existed = rating.models.ProjectRating.objects.create(
                user_id=user_id,
                project_id=project_id,
            )
        existed.score = rating_.score
        if commit:
            existed.save()
        return existed

    class Meta:
        model = rating.models.ProjectRating

        fields = [
            rating.models.ProjectRating.score.field.name,
        ]
        widgets = {
            rating.models.ProjectRating.score.field.name: RangeInput(
                attrs={
                    'id': 'rating-range',
                    'class': 'form-range',
                    'min': rating.models.ProjectRating.ScoreData.MIN,
                    'max': rating.models.ProjectRating.ScoreData.MAX,
                    'default': rating.models.ProjectRating.ScoreData.DEFAULT,
                },
            )
        }
