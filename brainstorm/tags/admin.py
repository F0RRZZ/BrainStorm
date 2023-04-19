import django.contrib.admin

import tags.models

django.contrib.admin.site.register(tags.models.Tag)
