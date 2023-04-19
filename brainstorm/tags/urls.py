import django.urls

import tags.views

app_name = 'tags'
urlpatterns = [
    django.urls.path('list/', tags.views.TagsListView.as_view(), name='list')
]
