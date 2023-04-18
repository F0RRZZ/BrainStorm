import django.db.models

import projects.models
import tags.models
import users.models


class ProjectManager(django.db.models.Manager):
    def get_for_feed(self):
        return (
            self.get_queryset()
            .select_related('preview')
            .prefetch_related(
                django.db.models.Prefetch(
                    projects.models.Project.tags.field.name,
                    queryset=tags.models.Tag.objects.filter(
                        is_published=True
                    ).only(tags.models.Tag.name.field.name),
                )
            )
        )

    def archive(self):
        return self.get_queryset().filter(in_archive=True, published=True)

    def new(self):
        return (
            self.get_queryset()
            .filter(in_archive=False, published=True)
            .select_related(
                projects.models.Project.author.field.name,
                'preview',
            )
            .only(
                f'{projects.models.Project.author.field.name}__'
                f'{users.models.User.username.field.name}',
                projects.models.Project.name.field.name,
                f'{projects.models.Project.author.field.name}__id',
                f'{projects.models.Project.tags.field.name}__'
                f'{tags.models.Tag.name.field.name}',
                projects.models.Project.short_description.field.name,
            )
            .order_by(f'-{projects.models.Project.creation_date.field.name}')
        )

    def best(self):
        return (
            self.get_queryset()
            .filter(in_archive=False, published=True)
            .annotate(score=django.db.models.Avg('score_project__score'))
            .select_related(
                projects.models.Project.author.field.name, 'preview'
            )
            .order_by('-score')
            .only(
                f'{projects.models.Project.author.field.name}__'
                f'{users.models.User.username.field.name}',
                projects.models.Project.name.field.name,
                f'{projects.models.Project.author.field.name}__id',
                f'{tags.models.Tag.name.field.name}',
                projects.models.Project.short_description.field.name,
            )
        )

    def speaked(self):
        return (
            self.get_queryset()
            .filter(in_archive=False, published=True)
            .annotate(django.db.models.Count('comments'))
            .select_related(
                projects.models.Project.author.field.name, 'preview'
            )
            .order_by('-comments__count')
            .only(
                f'{projects.models.Project.author.field.name}__'
                f'{users.models.User.username.field.name}',
                projects.models.Project.name.field.name,
                f'{projects.models.Project.author.field.name}__id',
                f'{tags.models.Tag.name.field.name}',
                projects.models.Project.short_description.field.name,
            )
        )

    def get_user_projects(self, user_id):
        return self.get_for_feed().filter(author_id=user_id)

    def get_author(self):
        return self.select_related(
            projects.models.Project.author.field.name
        ).only(
            'id',
            users.models.User.username.field.name,
        )

    def get_gallery_images(self):
        return self.prefetch_related('images_gallery')

    def get_preview(self):
        return self.select_related('preview').only('image')

    def get_comments(self):
        return self.prefetch_related('comments')

    def get_for_collaborator(self, user_id):
        return self.prefetch_related(
            django.db.models.Prefetch(
                projects.models.Project.collaborators.field.name,
                queryset=users.models.User.objects.only(
                    users.models.User.id.field.name,
                ),
            )
        ).filter(collaborators__id__contains=user_id)
