from django.db import models
from django.utils import timezone


class DailyReport(models.Model):
    # The 'date' field stores the date for the report. It defaults to the current date if not provided.
    # The field is marked as unique, ensuring only one report can exist per day.
    date = models.DateField(default=timezone.now, unique=True)
    
    # The 'total_orders' field stores the total number of orders for the given day.
    total_orders = models.PositiveIntegerField()
    
    # The 'total_income' field stores the total income generated from orders for the given day.
    # It is a decimal field with two decimal places, allowing for monetary values.
    total_income = models.DecimalField(max_digits=10, decimal_places=2)
    
    # The 'most_sold_item' field stores the name of the most sold item on that day.
    # It is optional (blank=True) as not every report may have this information.
    most_sold_item = models.CharField(max_length=255, blank=True)

    # The __str__ method provides a human-readable string representation of the object.
    # This helps in displaying the report information in Django's admin interface and elsewhere.
    def __str__(self):
        return f"Report - {self.date}"
