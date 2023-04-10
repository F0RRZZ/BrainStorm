from django.core.validators import MaxLengthValidator, ValidationError
from django.db import models

from core.tools import name_formatter


class Tag(models.Model):
    is_published = models.BooleanField('published', default=True)
    name = models.CharField(
        'название',
        max_length=150,
        help_text='Максимум 150 символов',
    )
    description = models.TextField(
        'описание',
        max_length=300,
        help_text='Описание. Максимум 300 символов',
    )
    slug = models.SlugField(
        'slug',
        validators=[
            MaxLengthValidator(200),
        ],
        unique=True,
        help_text='Максимум 200 символов',
    )
    formatted_name = models.CharField(
        'formatted name',
        max_length=150,
        editable=False,
    )

    class Meta:
        default_related_name = 'tags'
        verbose_name = 'тег'
        verbose_name_plural = 'теги'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.formatted_name = name_formatter(self.name)
        super().save(*args, **kwargs)

    def clean(self):
        formatted_name = name_formatter(self.name)
        if self.__class__.objects.filter(
            formatted_name=formatted_name
        ).exists():
            raise ValidationError('Название должно быть уникальным')
        return self.name
