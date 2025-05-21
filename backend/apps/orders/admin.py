from django.contrib import admin
from .models import Order, OrderItem


# The admin.site.register function is used to register the Order model with the admin panel.
# This allows you to view and manage all data related to the Order model in the admin interface.
admin.site.register(Order)

# The admin.site.register function is used to register the OrderItem model with the admin panel.
# This allows you to view and manage all data related to the OrderItem model in the admin interface.
admin.site.register(OrderItem)
