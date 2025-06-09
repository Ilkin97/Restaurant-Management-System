from rest_framework import viewsets
from apps.tables.models import Table
from .serializers import TableSerializer


class TableViewSet(viewsets.ModelViewSet):
    """
    Viewset for handling CRUD operations on 'Table' model instances.
    
    This viewset provides actions like list, create, retrieve, update, 
    and destroy for the 'Table' model using the associated 'TableSerializer'.
    The table entries are ordered by the 'number' field.
    """
    
    # Queryset to retrieve all Table instances, ordered by the 'number' field
    queryset = Table.objects.all().order_by('number')
    
    # Specify which serializer to use for the Table model
    serializer_class = TableSerializer
