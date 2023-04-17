import django.db.models

import collaboration.models


class CollaborationRequestManager(django.db.models.Manager):
    def get_for_project(self, project_id):
        return self.filter(project_id=project_id).order_by(
            f"""-{(
                collaboration.models.CollaborationRequest.creation_date.field.name
            )}""",
        )

    def get_for_user(self, user_id):
        return self.filter(user_id=user_id).order_by(
            f"""-{(
                collaboration.models.CollaborationRequest.creation_date.field.name
            )}""",
        )
