from rest_framework import viewsets
from apps.feedback.models import Feedback
from .serializers import FeedbackSerializer


class FeedbackViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing feedback instances.

    This viewset automatically provides 'list', 'create', 'retrieve', 'update', and 'destroy' actions for the Feedback model.
    It retrieves the feedback in descending order based on their creation date, meaning the most recent feedback comes first.
    """
    # Queryset to retrieve all feedback entries, ordered by creation date (most recent first)
    queryset = Feedback.objects.all().order_by('-created_at')

    # The serializer class used to convert the model instances to JSON format
    serializer_class = FeedbackSerializer
