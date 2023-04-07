import django.conf
import django.conf.urls.static
import django.contrib.admin
import django.contrib.auth.urls
import django.urls

urlpatterns = [
    django.urls.path(
        'projects/',
        django.urls.include('projects.urls')
    ),
    django.urls.path(
        '',
        django.urls.include('core.urls', namespace='core'),
    ),
    django.urls.path(
        'feed/',
        django.urls.include('feeds.urls', namespace='feeds'),
    ),
    django.urls.path(
        'feedback/',
        django.urls.include('feedback.urls', namespace='feedback'),
    ),
    django.urls.path(
        'about/',
        django.urls.include('about.urls', namespace='about'),
    ),
    django.urls.path(
        'tags/',
        django.urls.include('tags.urls', namespace='tags'),
    ),
    django.urls.path(
        'auth/',
        django.urls.include('users.urls', namespace='users'),
    ),
    django.urls.path(
        'auth/',
        django.urls.include(django.contrib.auth.urls),
    ),
    django.urls.path(
        'admin/',
        django.contrib.admin.site.urls,
    ),
]

urlpatterns += django.conf.urls.static.static(
    django.conf.settings.MEDIA_URL,
    document_root=django.conf.settings.MEDIA_ROOT,
)

if django.conf.settings.DEBUG:
    import debug_toolbar
    
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
