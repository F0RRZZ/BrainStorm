from django.views.generic import ListView
from tags.models import Tag


class TagsListView(ListView):
    model = Tag
    template_name = 'tags/list.html'
    context_object_name = 'tags'

    def get_queryset(self):
        return Tag.objects.all()
