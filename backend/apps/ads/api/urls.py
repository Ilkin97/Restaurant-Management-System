from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdvertisementViewSet


# Initialize the router
router = DefaultRouter()

# Register the AdvertisementViewSet with the router
# The AdvertisementViewSet will handle CRUD operations for the Advertisement model.
router.register(r'', AdvertisementViewSet)

# URL patterns for the advertisement endpoints
urlpatterns = [
    # Include the router's URLs for AdvertisementViewSet
    path('', include(router.urls)),
]
