import django.db.models
import sorl.thumbnail


def directory_path(instance, filename):
    path = f'{instance.project.name}_{instance.project.author.id}'
    return f'{path}/{filename}'


class ProjectImage(django.db.models.Model):
    image = django.db.models.ImageField(
        'фотка',
        upload_to=directory_path
    )

    def get_image_300x300(self, size='300x300'):
        return (
            sorl.thumbnail
            .get_thumbnail(self.image, size, crop='center', quality=51)
        )

    def __str__(self):
        return self.image.url

    class Meta:
        abstract = True
