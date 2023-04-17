import sorl.thumbnail


class ImageMixin:
    @property
    def get_image_150x150(self):
        return self.get_sized_image('150x150')

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
            self.__class__.DEFAULT_IMAGE,
            size,
            crop='center',
            quality=99,
        )

    def __str__(self):
        return self.image.url
