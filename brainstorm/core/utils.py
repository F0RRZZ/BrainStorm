import sorl.thumbnail


class ImageMixin:
    def get_image_300x300(self, size='300x300'):
        return sorl.thumbnail.get_thumbnail(
            self.image, size, crop='center', quality=51
        )

    def __str__(self):
        return self.image.url
