import django.db.models

import projects.models
import tags.models
import users.models


class ProjectManager(django.db.models.Manager):
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .select_related('preview')
            .prefetch_related(
                django.db.models.Prefetch(
                    'tags',
                    queryset=tags.models.Tag.objects.filter(
                        is_published=True
                    ).only('name'),
                )
            )
            .only(
                'id', 'tags__id', 'author__id',
                'author__username', 'preview__image', 'short_description'
            )
        )

    def archive(self):
        return (
            self.get_queryset()
            .filter(in_archive=True, published=True)
        )

    def new(self):
        return (
            self.get_queryset()
            .filter(in_archive=False, published=True)
            .order_by('-creation_date')
        )

    def best(self):
        return (
            self.get_queryset()
            .filter(in_archive=False, published=True)
            .annotate(score=django.db.models.Avg('score_project__score'))
            .order_by('-score')
        )

    def speaked(self):
        return (
            self.get_queryset()
            .filter(in_archive=False, published=True)
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
