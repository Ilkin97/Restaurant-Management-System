from rest_framework import viewsets
from ..models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer


# OrderViewSet handles all operations (list, create, update, delete) for the Order model.
class OrderViewSet(viewsets.ModelViewSet):
    # The queryset is ordered to retrieve orders by creation date in descending order (latest orders come first).
    queryset = Order.objects.all().order_by('-created_at')
    # The serializer class is specified. This serializer will be used to convert the Order model data into JSON format.
    serializer_class = OrderSerializer


# OrderItemViewSet handles all operations for the OrderItem model.
class OrderItemViewSet(viewsets.ModelViewSet):
    # All order items are fetched for listing.
    queryset = OrderItem.objects.all()
    # The serializer class is specified. This serializer will be used to convert the OrderItem model data into JSON format.
    serializer_class = OrderItemSerializer
