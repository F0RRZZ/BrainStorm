import os

import celery
import celery.schedules

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'brainstorm.settings')

app = celery.Celery('brainstorm')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'collect-projects-every-week': {
        'task': 'feeds.tasks.put_in_archive',
        #  ----For testing----
        # 'schedule': celery.schedules.crontab(minute='*/1'),
        # ----Working version---
        'schedule': celery.schedules.crontab(hour=2, day_of_week='tuesday'),
    },
}
