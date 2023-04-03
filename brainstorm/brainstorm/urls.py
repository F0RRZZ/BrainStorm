from django.conf import settings
from django.conf.urls.static import static
import django.contrib.admin
import django.contrib.auth.urls
from django.urls import include, path

import brainstorm.settings

urlpatterns = [
    path('feed/', include('feeds.urls', namespace='feeds')),
    path('feedback/', include('feedback.urls', namespace='feedback')),
    path('tags/', include('tags.urls', namespace='tags')),
    path('auth/', include('users.urls', namespace='users')),
    path('auth/', include(django.contrib.auth.urls)),
    path('admin/', django.contrib.admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if brainstorm.settings.DEBUG:
    urlpatterns += path('__debug__/', include('debug_toolbar.urls'))
