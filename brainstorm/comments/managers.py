import django.db.models


class CommentsManager(django.db.models.Manager):
    def get_user_comments(self, user_id):
        return self.all()
