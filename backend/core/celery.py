from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set the Django settings module
# Specifies the settings file for the Django project.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

# Create the Celery application
# Starts a Celery application with the name "core".
app = Celery("core")

# Load the settings from Django
# Integrates Celery with Django settings.
# Loads settings prefixed with CELERY.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Automatically discover tasks in Django models and other modules
# Automatically discovers and registers Django tasks with Celery.
app.autodiscover_tasks()

# The application that Celery runs
@app.task(bind=True)
def debug_task(self):
    """
    A simple Celery task.
    Used to test if Celery is working correctly.
    """
    print('Request: {0!r}'.format(self.request))
