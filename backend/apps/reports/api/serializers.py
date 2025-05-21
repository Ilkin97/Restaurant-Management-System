from rest_framework import serializers
from ..models import DailyReport


class DailyReportSerializer(serializers.ModelSerializer):
    """
    Serializer for the DailyReport model.

    This serializer is used to convert the DailyReport model instances into JSON format and vice versa. 
    It provides a way to easily read and write the data in the DailyReport model through Django REST Framework.

    Attributes:
        model (class): Specifies the model this serializer will work with, in this case, the DailyReport model.
        fields (list): Specifies the fields of the model that will be included in the serialized data. 
                       Using '__all__' will include all the fields defined in the model.
    """
    
    class Meta:
        # Specifies the model to be used by the serializer and which fields to include
        model = DailyReport  # The model that the serializer works with
        fields = '__all__'    # Include all fields from the model in the serialized output
