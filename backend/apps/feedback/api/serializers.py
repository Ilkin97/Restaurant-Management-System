from rest_framework import serializers
from ..models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Feedback model.

    This serializer is responsible for converting the Feedback model
    instances into JSON format and vice versa. It includes all the fields 
    from the Feedback model and provides validation and deserialization 
    functionality.
    """

    class Meta:
        model = Feedback  # Specifies the model to serialize
        fields = '__all__'  # Serializes all fields of the Feedback model
