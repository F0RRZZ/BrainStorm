import django.conf
import sorl.thumbnail


class ImageMixin:
    @property
    def get_image_400x400(self):
        return self.get_sized_image('400x400')

    @property
    def get_image_300x300(self):
        return self.get_sized_image('300x300')

    @property
    def get_image_50x50(self):
        return self.get_sized_image('50x50')

    def get_sized_image(self, size):
        if self.image:
            return sorl.thumbnail.get_thumbnail(
                self.image, size, crop='center', quality=99
            )
        return sorl.thumbnail.get_thumbnail(
            django.conf.settings.DEFAULT_USER_IMAGE_PATH,
            size,
            crop='center',
            quality=99,
        )

    def __str__(self):
        return self.image.url
