from rest_framework import serializers
from ..models import Advertisement


class AdvertisementSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Advertisement model.

    This serializer is used to convert Advertisement model instances into 
    JSON format (serialization) and also to validate incoming data when 
    creating or updating Advertisement instances (deserialization).
    """

    class Meta:
        """
        Meta class that defines model and fields to be serialized.
        
        - `model`: The model associated with this serializer.
        - `fields`: List of fields to be included in the serialization.
        """
        model = Advertisement  # Model to be serialized
        fields = "__all__"  # Serialize all fields in the model
