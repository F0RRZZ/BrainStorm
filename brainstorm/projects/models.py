import django.contrib.auth.models
import django.db.models
import django.utils.safestring
import sorl.thumbnail


def directory_path(instance, filename):
    if type(instance) == Project:
        path = f'{instance.name}_{instance.author.id}'
    else:
        path = f'{instance.project.name}_{instance.project.author.id}'
    return f'{path}/{filename}'


class Project(django.db.models.Model):
    class Status(django.db.models.TextChoices):
        DEVELOPMENT = 'development', 'В разработке',
        READY = 'ready', 'Готов'

    author = django.db.models.ForeignKey(
        django.contrib.auth.models.User,
        on_delete=django.db.models.CASCADE,
        verbose_name='автор',
        help_text='Кто автор',
        related_name='project'
    )

    main_image = django.db.models.ImageField(
        'главная картинка',
        upload_to=directory_path,
        null=True,
        blank=True
    )

    def get_image_300x300(self, size='300x300'):
        return (
            sorl.thumbnail
            .get_thumbnail(self.main_image, size, crop='center', quality=51)
        )

    name = django.db.models.CharField(
        'название',
        help_text='Назовите продукт',
        max_length=150
    )
    description = django.db.models.TextField(
        'описание',
        help_text='Введите описание продукта',
    )
    collaborators = django.db.models.ManyToManyField(
        django.contrib.auth.models.User,
        verbose_name='коллабораторы',
        related_name='colleagues',
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
    # добавить теги
    # добавить комментарии
    status = django.db.models.CharField(
        'статус проетка',
        max_length=14,
        choices=Status.choices,
        default=Status.DEVELOPMENT,
    )
    creation_date = django.db.models.DateTimeField(
        'дата создания',
        auto_now_add=True
    )
    update_date = django.db.models.DateTimeField(
        'дата изменения',
        auto_now=True
    )

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    def image_tmb(self):
        if self.main_image:
            image_url = self.get_image_300x300('300x300').url
            return django.utils.safestring.mark_safe(
                f'<img src="{image_url}" width="50" height="50">'
            )
        return 'Нет изображения'

    image_tmb.short_description = 'превью'
    image_tmb.allow_tags = True


class ImagesGallery(django.db.models.Model):
    image = django.db.models.ImageField(
        'Будет приведено к разрешению 300x300',
        upload_to=directory_path,
    )

    def get_image_300x300(self, size='300x300'):
        return (
            sorl.thumbnail
            .get_thumbnail(self.image, size, quality=51)
        )

    project = django.db.models.ForeignKey(
        Project,
        verbose_name='продукт',
        on_delete=django.db.models.CASCADE,
    )

    class Meta:
        verbose_name = 'картинка'
        verbose_name_plural = 'картинки'

    def __str__(self):
        return self.image.url
