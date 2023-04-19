import django.contrib.admin
from django.utils.translation import gettext_lazy as _

import feedback.models


class PersonalDataInline(django.contrib.admin.StackedInline):
    model = feedback.models.PersonalData

    readonly_fields = (feedback.models.PersonalData.email.field.name,)


class FilesInline(django.contrib.admin.TabularInline):
    model = feedback.models.FeedbackFile

    readonly_fields = (feedback.models.FeedbackFile.file.field.name,)


@django.contrib.admin.register(feedback.models.Feedback)
class FeedbackAdmin(django.contrib.admin.ModelAdmin):
    @django.contrib.admin.display(description=_('text'))
    def short_text(self, obj):
        return obj.text[:50]

    list_display = (
        short_text,
        feedback.models.Feedback.status.field.name,
    )
    readonly_fields = (
        feedback.models.Feedback.subject.field.name,
        feedback.models.Feedback.text.field.name,
        feedback.models.Feedback.created_on.field.name,
    )
    inlines = (
        PersonalDataInline,
        FilesInline,
    )
