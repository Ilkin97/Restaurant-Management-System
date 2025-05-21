from django.db import models
from django.utils.text import slugify
from datetime import timedelta

class Table(models.Model):
    # The 'name' field represents the name of the table. It can be null or blank.
    name = models.CharField(max_length=2, null=True, blank=True)

    # The 'slug' field is automatically generated from the 'name' and is unique for each table.
    slug = models.SlugField(max_length=120, unique=True, blank=True)

    # 'reservated_at' stores the date and time when the table was reserved.
    # It is set to the current date and time when a new table record is created.
    reservated_at = models.DateTimeField(auto_now_add=True)

    # 'updated_at' stores the date and time when the table record was last updated.
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # The 'verbose_name_plural' is set to make the plural name for 'Table' appear as "Tables".
        verbose_name_plural = "Tables"

        # The 'ordering' option orders tables by the 'name' field in ascending order.
        ordering = ['name']

    def save(self, *args, **kwargs):
        # If a 'slug' is not provided, generate it based on the 'name'.
        if not self.slug:
            self.slug = slugify(self.name)

        # Save the table record to the database.
        super().save(*args, **kwargs)
    
    def __str__(self):
        # The string representation of a Table object will return the table's name.
        return self.name
