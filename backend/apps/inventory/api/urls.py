from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InventoryItemViewSet


# Initialize a DefaultRouter instance, which automatically generates URL routes 
# for the viewset actions like list, create, update, delete, etc.
router = DefaultRouter()
# Register the 'InventoryItemViewSet' with the router, associating it with the 
# base URL path (empty string '' means the root of this specific API endpoint).
router.register(r'', InventoryItemViewSet)

urlpatterns = [
    # Include the generated URLs for the InventoryItemViewSet under this path.
    # This allows the viewset to handle requests for the listed routes.
    path('', include(router.urls)),
]
