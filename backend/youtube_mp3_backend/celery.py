from __future__ import absolute_import, unicode_literals
import os
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from celery import Celery
else:
    from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'youtube_mp3_backend.settings')

app = Celery('youtube_mp3_backend')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
