from rest_framework import serializers
from apps.inventory.models import InventoryItem


class InventoryItemSerializer(serializers.ModelSerializer):
    """
    Serializer for the InventoryItem model.

    This serializer converts the InventoryItem model instances into JSON 
    format for API responses and validates incoming data when creating or 
    updating InventoryItem objects.
    """

    class Meta:
        model = InventoryItem
        """
        The model that this serializer is associated with.
        In this case, it will serialize instances of the InventoryItem model.
        """
        fields = '__all__'
        """
        Specifies which fields should be included in the serialized output.
        The special value '__all__' means all fields of the model will be included.
        """
