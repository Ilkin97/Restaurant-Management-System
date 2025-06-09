from rest_framework import viewsets
from apps.inventory.models import InventoryItem
from .serializers import InventoryItemSerializer


class InventoryItemViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling CRUD operations for InventoryItem objects.
    
    Provides actions to list, create, retrieve, update, and delete InventoryItem objects.
    This ViewSet uses the 'InventoryItemSerializer' for serializing the data and 
    querying all InventoryItem objects ordered by their 'name'.
    """
    # The queryset used to retrieve the inventory items from the database, ordered alphabetically by name.
    queryset = InventoryItem.objects.all().order_by('name')
    
    # The serializer class that converts the model data to JSON format and vice versa.
    serializer_class = InventoryItemSerializer
