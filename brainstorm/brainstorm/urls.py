import django.contrib.admin
from django.urls import include, path

import brainstorm.settings

urlpatterns = [
    path('feed/', include('feeds.urls', namespace='feeds')),
    path('admin/', django.contrib.admin.site.urls),
]

if brainstorm.settings.DEBUG:
    urlpatterns += path('__debug__/', include('debug_toolbar.urls'))
