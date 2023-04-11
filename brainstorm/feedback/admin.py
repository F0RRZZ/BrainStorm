from django.contrib import admin

import feedback.models


@admin.register(feedback.models.Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = (
        'short_text',
        feedback.models.Feedback.status.field.name,
    )
    readonly_fields = (feedback.models.Feedback.created_on.field.name,)

    @admin.display(description='Текст')
    def short_text(self, obj):
        return obj.text[:50]
