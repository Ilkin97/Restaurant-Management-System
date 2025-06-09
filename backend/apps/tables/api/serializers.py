from rest_framework import serializers
from apps.tables.models import Table


class TableSerializer(serializers.ModelSerializer):
    """
    Serializer for the Table model. 
    It converts Table model instances into JSON format and vice versa.
    """

    class Meta:
        # The 'model' attribute links the serializer to the 'Table' model.
        model = Table
        
        # The 'fields' attribute defines which fields from the Table model should be included in the serializer.
        # The value '__all__' means all fields of the Table model will be included.
        fields = '__all__'
