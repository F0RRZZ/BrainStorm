import django.db.models

import projects.models
import tags.models
import users.models

SCORE_FIELD_NAME = 'score'
SCORE_PROJECT_FIELD_NAME = 'score_project'
COMMENTS_FIELD_NAME = 'comments'
IMAGES_GALLERY_FIELD_NAME = 'images_gallery'


class ProjectManager(django.db.models.Manager):
    def get_with_preview_and_tags(self):
        return (
            self.get_queryset()
            .select_related(projects.models.Project.preview.related.name)
            .prefetch_related(
                django.db.models.Prefetch(
                    projects.models.Project.tags.field.name,
                    queryset=tags.models.Tag.objects.filter(
                        is_published=True
                    ).only(tags.models.Tag.name.field.name),
                )
            )
        )

    def get_for_feed(self):
        return (
            self.get_with_preview_and_tags()
            .select_related(
                projects.models.Project.author.field.name,
            )
            .filter(published=True)
            .only(
                f'{projects.models.Project.author.field.name}__'
                f'{users.models.User.username.field.name}',
                projects.models.Project.name.field.name,
                f'{projects.models.Project.author.field.name}__'
                f'{projects.models.Project.id.field.name}',
                f'{projects.models.Project.tags.field.name}__'
                f'{tags.models.Tag.name.field.name}',
                projects.models.Project.short_description.field.name,
            )
        )

    def archive(self):
        return self.get_for_feed().filter(in_archive=True)

    def new(self):
        return (
            self.get_for_feed()
            .filter(in_archive=False)
            .order_by(f'-{projects.models.Project.creation_date.field.name}')
        )

    def best(self):
        return (
            self.get_for_feed()
            .filter(in_archive=False)
            .annotate(
                score=django.db.models.Avg(
                    f'{SCORE_PROJECT_FIELD_NAME}__{SCORE_FIELD_NAME}'
                )
            )
            .order_by(f'-{SCORE_FIELD_NAME}')
        )

    def speaked(self):
        return (
            self.get_for_feed()
            .filter(in_archive=False)
            .annotate(django.db.models.Count(COMMENTS_FIELD_NAME))
            .order_by(
                f'-{COMMENTS_FIELD_NAME}__count',
            )
        )

    def get_for_project_detail(self):
        return (
            self.get_with_preview_and_tags()
            .filter(published=True)
            .select_related(projects.models.Project.author.field.name)
            .prefetch_related(
                django.db.models.Prefetch(
                    IMAGES_GALLERY_FIELD_NAME,
                    queryset=projects.models.ImagesGallery.objects.only(
                        projects.models.ImagesGallery.image.field.name,
                        projects.models.ImagesGallery.project_id.field.name,
                    ),
                ),
                django.db.models.Prefetch(
                    projects.models.Project.collaborators.field.name,
                    queryset=users.models.User.objects.only(
                        users.models.User.username.field.name,
                    ),
                ),
            )
            .only(
                projects.models.Project.name.field.name,
                projects.models.Project.description.field.name,
                projects.models.Project.short_description.field.name,
                projects.models.Project.status.field.name,
                projects.models.Project.creation_date.field.name,
                projects.models.Project.update_date.field.name,
                f'{projects.models.Project.author.field.name}__'
                f'{users.models.User.username.field.name}',
                f'{projects.models.Project.preview.related.name}__'
                f'{projects.models.Preview.image.field.name}',
            )
        )

    def get_for_user_detail(self, user_id):
        return (
            self.get_for_feed()
            .filter(author_id=user_id)
            .order_by(f'-{projects.models.Project.creation_date.field.name}')
        )

    def get_for_user_detail_by_collaborator(self, user_id):
        return (
            self.get_for_feed()
            .prefetch_related(
                django.db.models.Prefetch(
                    projects.models.Project.collaborators.field.name,
                    queryset=users.models.User.objects.only(
                        users.models.User.id.field.name,
                    ),
                )
            )
            .filter(collaborators__id__contains=user_id)
            .order_by(f'-{projects.models.Project.creation_date.field.name}')
        )

    def get_for_redact(self):
        return (
            self.select_related(projects.models.Project.preview.related.name)
            .prefetch_related(
                django.db.models.Prefetch(
                    projects.models.Project.tags.field.name,
                    queryset=tags.models.Tag.objects.get_for_select(),
                ),
                django.db.models.Prefetch(
                    IMAGES_GALLERY_FIELD_NAME,
                    queryset=projects.models.ImagesGallery.objects.only(
                        projects.models.ImagesGallery.image.field.name,
                    ),
                ),
            )
            .only(
                projects.models.Project.name.field.name,
                projects.models.Project.description.field.name,
                projects.models.Project.short_description.field.name,
                projects.models.Project.status.field.name,
                f'{projects.models.Project.preview.related.name}__'
                f'{projects.models.Preview.image.field.name}',
            )
        )

    def get_gallery_images(self):
        return self.prefetch_related(IMAGES_GALLERY_FIELD_NAME)

    def get_preview(self):
        return self.select_related(
            projects.models.Project.preview.related.name
        ).only(projects.models.Preview.image.field.name)

    def get_comments(self):
        return self.prefetch_related(COMMENTS_FIELD_NAME)
