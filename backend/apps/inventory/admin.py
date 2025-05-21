from django.contrib import admin
from .models import InventoryItem


# Register the InventoryItem model with the Django admin site.
# This allows you to manage InventoryItem objects through the Django admin interface.
admin.site.register(InventoryItem)
