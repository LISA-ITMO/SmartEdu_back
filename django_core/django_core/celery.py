from __future__ import absolute_import, unicode_literals

import os
from django.core import management
from django.conf import settings

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_core.settings")

app = Celery("django_core")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
