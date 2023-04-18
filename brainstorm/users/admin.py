import django.contrib.admin

import users.models


@django.contrib.admin.register(users.models.User)
class ProjectAdmin(django.contrib.admin.ModelAdmin):
    exclude = [
        users.models.User.password.field.name,
        users.models.User.normalized_email.field.name,
    ]
