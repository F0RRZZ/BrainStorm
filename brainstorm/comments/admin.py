import comments.models
import django.contrib.admin


@django.contrib.admin.register(comments.models.Comment)
class CommentAdmin(django.contrib.admin.ModelAdmin):
    list_display = (
        comments.models.Comment.user.field.name,
        comments.models.Comment.text.field.name,
    )

    list_display_links = (comments.models.Comment.user.field.name,)
