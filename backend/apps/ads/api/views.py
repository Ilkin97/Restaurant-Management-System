from rest_framework import viewsets
from apps.ads.models import Advertisement
from .serializers import AdvertisementSerializer


class AdvertisementViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Advertisement instances.

    This viewset provides the standard actions like:
    - List: GET /api/advertisements/
    - Retrieve: GET /api/advertisements/{id}/
    - Create: POST /api/advertisements/
    - Update: PUT /api/advertisements/{id}/
    - Destroy: DELETE /api/advertisements/{id}/
    """
    
    # Queryset to retrieve all advertisements ordered by creation date (newest first)
    queryset = Advertisement.objects.all().order_by('-created_at')

    # Serializer class to convert Advertisement instances to JSON format
    serializer_class = AdvertisementSerializer
