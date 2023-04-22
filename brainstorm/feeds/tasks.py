from brainstorm.celery import app
import projects.models
import rating.models


@app.task
def put_in_archive():
    for project in projects.models.Project.objects.all():
        score = rating.models.ProjectRating.objects.get_avg_rating(project.id)
        if score != '?' and score < 5:
            project.in_archive = True
        else:
            project.in_archive = False
        project.save(update_fields=['in_archive'])
