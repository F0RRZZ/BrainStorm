import django.db.models
from django.utils.translation import gettext_lazy as _


class PersonalData(django.db.models.Model):
    email = django.db.models.EmailField(
        _('user_email'),
        max_length=254,
        help_text=_('type_email_on_what_answer_will_be_sent__lowercase'),
    )


class Feedback(django.db.models.Model):
    class Status(django.db.models.TextChoices):
        RECIEVED = ('received', 'получено')
        PROCESSING = ('processing', 'в обработке')
        ANSWERED = ('answered', 'ответ дан')

    subject = django.db.models.CharField(
        _('subject'),
        max_length=200,
    )
    text = django.db.models.TextField(
        _('message'),
    )
    created_on = django.db.models.DateTimeField(
        _('creation_date'),
        auto_now_add=True,
    )
    personal_data = django.db.models.OneToOneField(
        PersonalData,
        on_delete=django.db.models.CASCADE,
        blank=True,
        null=True,
    )
    status = django.db.models.CharField(
        _('status'),
        max_length=20,
        choices=Status.choices,
        default=Status.RECIEVED,
    )

    class Meta:
        verbose_name = _('feedback')
        verbose_name_plural = _('feedbacks')


class FeedbackFile(django.db.models.Model):
    file = django.db.models.FileField(
        blank=True,
        null=True,
    )
    feedback = django.db.models.ForeignKey(
        Feedback,
        on_delete=django.db.models.CASCADE,
        related_name='feedback_files',
    )
