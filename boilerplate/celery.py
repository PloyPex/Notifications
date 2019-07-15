from __future__ import print_function, absolute_import

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'boilerplate.settings')

app = Celery('boilerplate')

app.conf.update(
	task_routes={
		'notifications.tasks.send_notification_email': {'queue': 'notifications'},
	},
)

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
