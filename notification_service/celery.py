import os
from celery import Celery

from .settings import INSTALLED_APPS

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "notification_service")

app = Celery("notification_service")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(lambda: INSTALLED_APPS)
