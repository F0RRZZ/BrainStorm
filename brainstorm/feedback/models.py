from django.db import models


class Feedback(models.Model):
    CHOICES = [
        ('received', 'получено'),
        ('processing', 'в обработке'),
        ('answered', 'ответ дан'),
    ]
    subject = models.CharField('subject', max_length=200, help_text='тема',)
    text = models.TextField('text', help_text='содержание письма',)
    created_on = models.DateTimeField(
        'created_on', auto_now_add=True, help_text='время создания отзыва',
    )
    personal_data = models.OneToOneField(
        'PersonalData',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    status = models.CharField(
        'status',
        max_length=20,
        choices=CHOICES,
        default='received',
    )

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class FeedbackFile(models.Model):
    file = models.FileField(
        blank=True,
        null=True,
    )
    feedback = models.ForeignKey(
        Feedback,
        on_delete=models.CASCADE,
        related_name='feedback_files',
    )


class PersonalData(models.Model):
    email = models.EmailField(
        'email',
        max_length=254,
        help_text='введите почту, на которую будет отправлен ответ',
    )
