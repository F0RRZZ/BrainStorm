import django.db.models


class CommentsManager(django.db.models.Manager):
    def get_user_comments(self, user_id):
        return (
            self.filter(user_id=user_id)
            .select_related('user')
            .only(
                'text',
                'user__username',
                'user__image',
                'creation_date',
            )
        )

    def get_project_comments(self, project_id):
        return (
            self.filter(project_id=project_id)
            .select_related('user')
            .prefetch_related('project')
            .only(
                'text',
                'user__username',
                'user__image',
                'creation_date',
                'project__id',
            )
        )
