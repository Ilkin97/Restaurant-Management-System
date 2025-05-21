from django.db import models


class InventoryItem(models.Model):
    """
    A model to represent an inventory item with its name, quantity,
    unit of measurement, and the date when it was last updated.
    """
    name = models.CharField(max_length=100, unique=True)
    quantity = models.FloatField()
    unit = models.CharField(
        max_length=20,
        choices=[  # Define the unit choices for the inventory item
            ('kg', 'Kilogram'),
            ('g', 'Gram'),
            ('l', 'Litre'),
            ('ml', 'Millilitre'),
            ('pcs', 'Pieces'),
        ]
    )
    updated_at = models.DateTimeField(auto_now=True)  # Automatically update the timestamp whenever the record is modified

    def __str__(self):
        """
        String representation of the InventoryItem object.
        Returns a string with the item name, quantity, and unit of measurement.
        """
        return f"{self.name} - {self.quantity} {self.unit}"
