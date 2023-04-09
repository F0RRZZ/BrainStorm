import sorl.thumbnail


class ImageMixin:
    def get_image_300x300(self, size='300x300'):
        return sorl.thumbnail.get_thumbnail(
            self.image, size, crop='center', quality=51
        )

    @property
    def get_image_50x50(self):
        if self.image:
            return sorl.thumbnail.get_thumbnail(
                self.image, '50x50', crop='center', quality=51
            )
        return sorl.thumbnail.get_thumbnail(
            'static/img/user_default.jpg', '50x50', crop='center', quality=51
        )

    def __str__(self):
        return self.image.url
