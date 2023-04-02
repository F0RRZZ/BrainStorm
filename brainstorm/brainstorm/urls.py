"""brainstorm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import django.contrib.admin
import django.urls

import brainstorm.settings

urlpatterns = [
    django.urls.path('admin/', django.contrib.admin.site.urls),
    django.urls.path('projects/', django.urls.include('projects.urls')),
]

if brainstorm.settings.DEBUG:
    urlpatterns += [
        django.urls.path(
            '__debug__/',
            django.urls.include('debug_toolbar.urls'),
        ),
    ]
