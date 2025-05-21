from django.contrib import admin
from .models import Advertisement


# Registering the Advertisement model to be accessible in the Django admin interface
admin.site.register(Advertisement)
