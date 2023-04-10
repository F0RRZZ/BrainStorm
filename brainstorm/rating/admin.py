import django.contrib.admin
import rating.models


@django.contrib.admin.register(rating.models.ProjectRating)
class ProjectRatingAdmin(django.contrib.admin.ModelAdmin):
    list_display = (
        rating.models.ProjectRating.project.field.name,
        rating.models.ProjectRating.score.field.name,
    )


@django.contrib.admin.register(rating.models.CommentRating)
class CommentRatingAdmin(django.contrib.admin.ModelAdmin):
    list_display = (
        rating.models.CommentRating.comment.field.name,
        rating.models.CommentRating.score.field.name,
    )
