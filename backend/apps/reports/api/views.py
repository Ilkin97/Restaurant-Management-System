from rest_framework import viewsets
from ..models import DailyReport
from .serializers import DailyReportSerializer


class DailyReportViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the CRUD operations (Create, Read, Update, Delete) for DailyReport model.
    
    The queryset retrieves all DailyReport objects, ordered by date in descending order.
    The serializer converts DailyReport model instances to JSON format, and vice versa.
    """
    
    # Define the queryset that will be used for retrieving DailyReport objects.
    # The reports are ordered by 'date' in descending order so the most recent reports appear first.
    queryset = DailyReport.objects.all().order_by('-date')
    
    # Define the serializer class to be used for serializing the data.
    # This will convert the DailyReport model instances into JSON and vice versa.
    serializer_class = DailyReportSerializer
