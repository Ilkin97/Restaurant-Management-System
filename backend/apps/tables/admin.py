from django.contrib import admin
from .models import Table

# Registering the Table model in the admin site.
# This allows the model to be managed through Django's admin interface.
admin.site.register(Table)
