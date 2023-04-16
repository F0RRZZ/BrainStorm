import django.db.models

import projects.models
import tags.models
import users.models


class ProjectManager(django.db.models.Manager):
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(published=True)
            .select_related('preview')
            .prefetch_related(
                django.db.models.Prefetch(
                    'tags',
                    queryset=tags.models.Tag.objects.filter(
                        is_published=True
                    ).only('name'),
                )
            )
            .only('name', 'short_description', 'author__id', 'tags__name')
        )

    def archive(self):
        return self.get_queryset().filter(in_archive=True)

    def new(self):
        return self.get_queryset().order_by('-creation_date')

    def best(self):
        return self.get_queryset().order_by('-score_project__score')

    def speaked(self):
        return (
            self.get_queryset()
            .annotate(django.db.models.Count('comments'))
            .order_by('-comments__count')
        )

    def get_user_projects(self, user_id):
        return self.filter(author_id=user_id)

    def get_for_collaborator(self, user_id):
        return self.prefetch_related(
            django.db.models.Prefetch(
                projects.models.Project.collaborators.field.name,
                queryset=users.models.User.objects.only(
                    users.models.User.id.field.name,
                ),
            )
        ).filter(collaborators__id__contains=user_id)

    def get_avg_rating(self, project_id):
        return 8.6
