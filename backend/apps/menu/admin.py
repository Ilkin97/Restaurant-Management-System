from django.contrib import admin
from .models import Category, Product, Favorite

# Registering the Category model to the Django admin panel.
# This allows the Category model to be managed via the admin interface.
admin.site.register(Category)

# Registering the Product model to the Django admin panel.
# This allows the Product model to be managed via the admin interface.
admin.site.register(Product)

# Registering the Favorite model to the Django admin panel.
# This allows the Favorite model to be managed via the admin interface.
admin.site.register(Favorite)
