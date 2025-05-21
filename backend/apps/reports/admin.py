from django.contrib import admin
from .models import DailyReport


# Register the DailyReport model to make it accessible in the Django admin interface.
# This allows the admin users to view, create, edit, and delete DailyReport objects from the admin panel.
admin.site.register(DailyReport)
