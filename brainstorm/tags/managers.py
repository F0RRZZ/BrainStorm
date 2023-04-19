import django.db.models

import tags.models


class TagManager(django.db.models.Manager):
    def get_for_select(self):
        return self.filter(is_published=True).only(
            tags.models.Tag.name.field.name,
            tags.models.Tag.slug.field.name,
        )
