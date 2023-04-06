import django.urls

import core.views

app_name = 'core'
urlpatterns = [
    django.urls.path(
        '',
        core.views.TestView.as_view(),
        name='main',
    ),
    django.urls.path(
        '<path:template>/',
        core.views.TestView.as_view(),
        name='test_templates',
    ),
]
