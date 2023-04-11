import django.db.models


class ProjectManager(django.db.models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(published=True)

    def archive(self):
        return self.get_queryset().filter(in_archive=True)

    def new(self):
        return self.get_queryset().order_by('-creation_date')

    def best(self):
        return self.get_queryset().order_by('-score_project__score')

    def get_avg_rating(self, project_id):
        return 8.6
