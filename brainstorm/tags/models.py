import django.core.exceptions
import django.core.validators
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.tools import name_formatter


class Tag(models.Model):
    is_published = models.BooleanField(
        _('published'),
        default=True,
    )
    name = models.CharField(
        _('name'),
        max_length=30,
        help_text=_('maximum_30_symbols'),
    )
    description = models.TextField(
        _('description'),
        max_length=400,
        help_text=_('maximum_400_symbols'),
    )
    slug = models.SlugField(
        'slug',
        validators=[
            django.core.validators.MaxLengthValidator(50),
        ],
        unique=True,
        help_text=_('maximum_50_symbols'),
    )
    formatted_name = models.CharField(
        _('normalized_name'),
        max_length=35,
        editable=False,
    )

    class Meta:
        default_related_name = 'tags'
        verbose_name = _('tag')
        verbose_name_plural = _('tags')

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
            raise django.core.exceptions.ValidationError(
                _('name_must_be_unique')
            )
        return self.name
