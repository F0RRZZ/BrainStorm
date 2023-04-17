import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'brainstorm.settings')

app = Celery('brainstorm')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'collect-projects-every-week': {
        'task': 'feeds.tasks.put_in_archive',
        #  ----Для теста----
        # 'schedule': crontab(minute='*/1'),
        # ----Рабочая версия---
        'schedule': crontab(hour=2, day_of_week='tuesday'),
    },
}
