import django.db.models

import tags.models


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
        return (
            self.get_queryset()
            .filter(in_archive=False)
            .select_related('author', 'preview')
            .order_by('-creation_date')
            .only(
                'author__username',
                'name',
                'author__id',
                'tags__name',
                'short_description',
            )
        )

    def best(self):
        return (
            self.get_queryset()
            .annotate(score=django.db.models.Avg('score_project__score'))
            .filter(in_archive=False)
            .select_related('author', 'preview')
            .order_by('-score')
            .only(
                'author__username',
                'name',
                'author__id',
                'tags__name',
                'short_description',
            )
        )

    def speaked(self):
        return (
            self.get_queryset()
            .annotate(django.db.models.Count('comments'))
            .filter(in_archive=False)
            .select_related('author', 'preview')
            .order_by('-comments__count')
            .only(
                'author__username',
                'name',
                'author__id',
                'tags__name',
                'short_description',
            )
        )

    def get_user_projects(self, user_id):
        return self.filter(author_id=user_id)

    def get_gallery_images(self):
        return self.prefetch_related('images_gallery')

    def get_preview(self):
        return self.select_related('preview')
