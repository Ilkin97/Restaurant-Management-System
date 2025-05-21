from django.db import models
from apps.tables.models import Table
from apps.menu.models import Product


class Order(models.Model):
    """
    Represents an order placed at a table in a restaurant.

    The `Order` model contains the status of the order, which can be:
    - 'pending' : Order is created but not yet processed.
    - 'preparing' : Order is being prepared.
    - 'served' : Order has been served to the table.
    - 'cancelled' : Order was cancelled before it was processed.
    - 'paid' : Order has been paid.

    Attributes:
        table (ForeignKey): The table where the order was placed.
        status (CharField): The current status of the order, chosen from predefined options.
        created_at (DateTimeField): The timestamp when the order was created.
        updated_at (DateTimeField): The timestamp when the order was last updated.
    """
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('preparing', 'Preparing'),
        ('served', 'Served'),
        ('cancelled', 'Cancelled'),
        ('paid', 'Paid'),
    ]

    # ForeignKey link to the Table model, related to 'orders' on the Table model
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='orders')
    # Status field that holds the state of the order (using the choices defined above)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    # Automatically records the date and time when the order is created
    created_at = models.DateTimeField(auto_now_add=True)
    # Automatically updates the date and time when the order is modified
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Returns a string representation of the order.

        Format: "Order <id> - Table <table_number> (<status>)"
        """
        return f"Order {self.id} - Table {self.table.number} ({self.status})"


class OrderItem(models.Model):
    """
    Represents an individual item within an order.

    The `OrderItem` model stores information about which product was ordered, 
    how many of that product, and any special notes associated with the item.

    Attributes:
        order (ForeignKey): The order that this item belongs to.
        product (ForeignKey): The product that was ordered.
        quantity (PositiveIntegerField): The quantity of the product ordered.
        note (TextField): Any additional notes regarding the item (e.g., special requests).
    """

    # ForeignKey link to the Order model, each item is part of an order
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    # ForeignKey link to the Product model, represents the product ordered
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # Defines the quantity of the ordered product, with a default of 1
    quantity = models.PositiveIntegerField(default=1)
    # Allows a text field for special requests or instructions related to the product
    note = models.TextField(blank=True)

    def __str__(self):
        """
        Returns a string representation of the order item.

        Format: "{quantity} x {product_name} (Order {order_id})"
        """
        return f"{self.quantity} x {self.product.name} (Order {self.order.id})"
