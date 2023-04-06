import django.contrib.admin
import django.utils.safestring
import projects.models


class ImagesGalleryInline(django.contrib.admin.TabularInline):
    model = projects.models.ImagesGallery


class PreviewInline(django.contrib.admin.TabularInline):
    model = projects.models.Preview


@django.contrib.admin.register(projects.models.Project)
class ProjectAdmin(django.contrib.admin.ModelAdmin):
    list_display = (
        projects.models.Project.image_tmb,
        projects.models.Project.name.field.name,
        projects.models.Project.published.field.name,
        projects.models.Project.status.field.name,
    )
    list_editable = (
        projects.models.Project.published.field.name,
        projects.models.Project.status.field.name,
    )
    list_display_links = (projects.models.Project.name.field.name,)
    inlines = (
        ImagesGalleryInline,
        PreviewInline,
    )
    filter_horizontal = (projects.models.Project.collaborators.field.name,)
