import django.db.models

import comments.models
import projects.models
import users.models


class CommentsManager(django.db.models.Manager):
    def get_for_user_detail(self, user_id):
        return (
            self.filter(user_id=user_id)
            .select_related(comments.models.Comment.project.field.name)
            .only(
                comments.models.Comment.text.field.name,
                f'{comments.models.Comment.user.field.name}__'
                f'{users.models.User.username.field.name}',
                f'{comments.models.Comment.user.field.name}__'
                f'{users.models.User.image.field.name}',
                comments.models.Comment.creation_date.field.name,
                f'{comments.models.Comment.project.field.name}__'
                f'{projects.models.Project.name.field.name}',
            )
        )

    def get_project_comments(self, project_id):
        return (
            self.filter(project_id=project_id)
            .select_related(f'{comments.models.Comment.user.field.name}')
            .prefetch_related(f'{comments.models.Comment.project.field.name}')
            .only(
                comments.models.Comment.text.field.name,
                f'{comments.models.Comment.user.field.name}__'
                f'{users.models.User.username.field.name}',
                f'{comments.models.Comment.user.field.name}__'
                f'{users.models.User.image.field.name}',
                comments.models.Comment.creation_date.field.name,
                f'{comments.models.Comment.project.field.name}__id',
            )
            .order_by(
                f'-{comments.models.Comment.creation_date.field.name}',
            )
        )
