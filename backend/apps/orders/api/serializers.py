from rest_framework import serializers
from ..models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    """
    Serializer for the OrderItem model.

    This serializer defines how the OrderItem data is represented and serialized.
    It ensures that all fields in the OrderItem model are included in the serialized output.

    Fields:
        - Product: The product being ordered.
        - Quantity: The quantity of the product ordered.
        - Price: The price of the individual product.
    """
    
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer for the Order model.

    This serializer represents and serializes an Order, including all the related
    OrderItem instances. It allows for easy retrieval and modification of order data
    and includes the list of order items.

    Fields:
        - id: The unique identifier of the order.
        - customer: The customer who made the order.
        - created_at: The timestamp when the order was created.
        - status: The current status of the order (e.g., pending, completed).
        - items: A list of order items that belong to this order.
    """
    
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
