import django.db.models

import collaboration.managers
import projects.models
import users.models


class CollaborationRequest(django.db.models.Model):
    project = django.db.models.ForeignKey(
        projects.models.Project,
        on_delete=django.db.models.CASCADE,
        related_name='collaboration_requests',
    )
    user = django.db.models.ForeignKey(
        users.models.User,
        on_delete=django.db.models.CASCADE,
        related_name='collaboration_requests',
    )
    contact = django.db.models.TextField(max_length=150)
    about = django.db.models.TextField(blank=True)
    created_at = django.db.models.DateTimeField(auto_now_add=True)

    objects = collaboration.managers.CollaborationRequestManager()
