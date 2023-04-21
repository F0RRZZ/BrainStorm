import django.views.generic

import tags.models


class TagsListView(django.views.generic.ListView):
    model = tags.models.Tag
    template_name = 'tags/list.html'
    context_object_name = 'tags'

    def get_queryset(self):
        return tags.models.Tag.objects.get_ordered().only(
            tags.models.Tag.name.field.name,
            tags.models.Tag.description.field.name,
        )
