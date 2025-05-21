from django.contrib import admin
from .models import Feedback


# Register the Feedback model to the Django admin site
# This allows the model to be managed via Django's admin interface
admin.site.register(Feedback)
