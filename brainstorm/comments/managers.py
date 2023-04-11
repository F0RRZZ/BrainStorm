import django.db.models


class CommentsManager(django.db.models.Manager):
    def get_user_comments(self, user_id):
        return self.filter(user_id=user_id)

    def get_project_comments(self, project_id):
        return self.filter(project_id=project_id)
