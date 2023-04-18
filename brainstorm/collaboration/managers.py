import django.db.models

import collaboration.models
import projects.models
import users.models


class CollaborationRequestManager(django.db.models.Manager):
    def get_queryset(self):
        # We can`t use it in __init__ or as constants
        # Necessary for correct line length`
        self.PROJECT_FIELD_NAME = (
            collaboration.models.CollaborationRequest.project.field.name
        )
        self.USER_FIELD_NAME = (
            collaboration.models.CollaborationRequest.user.field.name
        )
        self.CREATION_DATE_FIELD_NAME = (
            collaboration.models.CollaborationRequest.creation_date.field.name
        )
        return super().get_queryset()

    def get_ordered_by_date(self):
        return self.order_by(
            f"""-{(
                (
                    collaboration.models.CollaborationRequest
                    .creation_date.field.name
                ),
            )}""",
        )

    def get_for_list(self, project_id):
        return (
            self.get_ordered_by_date()
            .filter(project_id=project_id)
            .select_related(
                self.USER_FIELD_NAME,
            )
            .only(
                collaboration.models.CollaborationRequest.about.field.name,
                collaboration.models.CollaborationRequest.status.field.name,
                self.CREATION_DATE_FIELD_NAME,
                '__'.join(
                    (
                        self.USER_FIELD_NAME,
                        users.models.User.USERNAME_FIELD,
                    )
                ),
                '__'.join(
                    (
                        self.USER_FIELD_NAME,
                        users.models.User.image.field.name,
                    )
                ),
            )
        )

    def get_for_my_list(self, user_id):
        return (
            self.get_ordered_by_date()
            .filter(user_id=user_id)
            .select_related(
                collaboration.models.CollaborationRequest.project.field.name,
            )
            .only(
                collaboration.models.CollaborationRequest.about.field.name,
                collaboration.models.CollaborationRequest.status.field.name,
                self.CREATION_DATE_FIELD_NAME,
                '__'.join(
                    (
                        self.PROJECT_FIELD_NAME,
                        projects.models.Project.name.field.name,
                    )
                ),
            )
        )

    def get_for_my_detail(self):
        return self.select_related(
            collaboration.models.CollaborationRequest.project.field.name,
        ).only(
            collaboration.models.CollaborationRequest.about.field.name,
            collaboration.models.CollaborationRequest.contact.field.name,
            collaboration.models.CollaborationRequest.status.field.name,
            collaboration.models.CollaborationRequest.creation_date.field.name,
            collaboration.models.CollaborationRequest.answer.field.name,
            collaboration.models.CollaborationRequest.user_id.field.name,
            '__'.join(
                (
                    self.PROJECT_FIELD_NAME,
                    projects.models.Project.name.field.name,
                )
            ),
        )

    def get_for_detail(self):
        return self.select_related(
            collaboration.models.CollaborationRequest.user.field.name,
            collaboration.models.CollaborationRequest.project.field.name,
        ).only(
            collaboration.models.CollaborationRequest.about.field.name,
            collaboration.models.CollaborationRequest.contact.field.name,
            collaboration.models.CollaborationRequest.status.field.name,
            collaboration.models.CollaborationRequest.creation_date.field.name,
            collaboration.models.CollaborationRequest.answer.field.name,
            '__'.join(
                (
                    self.PROJECT_FIELD_NAME,
                    projects.models.Project.name.field.name,
                )
            ),
            '__'.join(
                (
                    collaboration.models.CollaborationRequest.user.field.name,
                    users.models.User.USERNAME_FIELD,
                )
            ),
            '__'.join(
                (
                    collaboration.models.CollaborationRequest.user.field.name,
                    users.models.User.image.field.name,
                )
            ),
            '__'.join(
                (
                    collaboration.models.CollaborationRequest.user.field.name,
                    users.models.User.first_name.field.name,
                )
            ),
            '__'.join(
                (
                    collaboration.models.CollaborationRequest.user.field.name,
                    users.models.User.last_name.field.name,
                )
            ),
        )
