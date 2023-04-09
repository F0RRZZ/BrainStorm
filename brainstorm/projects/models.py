import django.contrib.auth.models
import django.db.models
import django.utils.safestring

import core.models
import tags.models
import users.models


class Project(django.db.models.Model):
    class Status(django.db.models.TextChoices):
        DEVELOPMENT = ('development', 'В разработке')
        READY = ('ready', 'Готов')

    author = django.db.models.ForeignKey(
        users.models.User,
        on_delete=django.db.models.CASCADE,
        related_name='projects',
        verbose_name='автор',
        help_text='Кто автор',
    )

    name = django.db.models.CharField(
        'название',
        help_text='Назовите проект',
        max_length=150,
    )
    short_description = django.db.models.TextField(
        'краткое описание',
        help_text='Введите краткое описание проекта',
    )
    description = django.db.models.TextField(
        'описание',
        help_text='Введите описание проекта',
    )
    collaborators = django.db.models.ManyToManyField(
        users.models.User,
        verbose_name='коллабораторы',
        related_name='colleagues',
        null=True,
        blank=True,
    )
    tags = django.db.models.ManyToManyField(
        tags.models.Tag,
        verbose_name='теги',
        related_name='projects',
        null=True,
        blank=True,
    )
    published = django.db.models.BooleanField(
        'опубликовано',
        default=True,
    )
    in_archive = django.db.models.BooleanField(
        'в архиве',
        default=False,
    )
    status = django.db.models.CharField(
        'статус проетка',
        max_length=14,
        choices=Status.choices,
        default=Status.DEVELOPMENT,
    )
    creation_date = django.db.models.DateTimeField(
        'дата создания',
        auto_now_add=True,
    )
    update_date = django.db.models.DateTimeField(
        'дата изменения',
        auto_now=True,
    )

    class Meta:
        verbose_name = 'проект'
        verbose_name_plural = 'проекты'

    def image_tmb(self):
        if self.preview:
            image_url = self.preview.get_image_300x300().url
            return django.utils.safestring.mark_safe(
                f'<img src="{image_url}" width="50" height="50">'
            )
        return 'Нет изображения'

    image_tmb.short_description = 'превью'
    image_tmb.allow_tags = True


class Preview(core.models.ProjectImage):
    project = django.db.models.OneToOneField(
        Project,
        verbose_name=Project._meta.verbose_name,
        help_text='Какому проекту принадлежит превью',
        on_delete=django.db.models.CASCADE,
        related_name='preview',
    )

    class Meta:
        verbose_name = 'превью'
        verbose_name_plural = 'превьюшки'

    def __str__(self):
        return self.image.url


class ImagesGallery(core.models.ProjectImage):
    project = django.db.models.ForeignKey(
        Project,
        verbose_name='продукт',
        on_delete=django.db.models.CASCADE,
        help_text='Какому проекту принадлежит картинка',
        related_name='images_gallery',
    )

    class Meta:
        verbose_name = 'галлерея'
        verbose_name_plural = 'галлереи'

    def __str__(self):
        return self.image.url
