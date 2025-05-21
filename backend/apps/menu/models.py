from django.db import models
from django.utils.text import slugify
from django.conf import settings


class Category(models.Model):
    """
    Model representing a product category.
    
    A category can have multiple products and includes a name, description,
    and slug for URL handling. Categories are ordered by their name.
    """
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def save(self, *args, **kwargs):
        """
        Override the save method to automatically generate a slug if not provided.
        """
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        """
        String representation of the Category instance.
        """
        return self.name


class Product(models.Model):
    """
    Model representing a product.
    
    Each product belongs to a category, has a name, description, price, and
    image. Products are ordered by their name and can be marked as available or not.
    """
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='menu/images/', blank=True, null=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def save(self, *args, **kwargs):
        """
        Override the save method to automatically generate a slug if not provided.
        """
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        """
        String representation of the Product instance.
        """
        return self.name


class Favorite(models.Model):
    """
    Model representing a user's favorite product.
    
    A favorite links a user and a product. The same user can have multiple
    favorites, but a product can only be added once to a user's favorites.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='favorites')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='favorited_by')
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')
        ordering = ['-added_at']

    def __str__(self):
        """
        String representation of the Favorite instance.
        """
        return f"{self.user.username} loves {self.product.name}"
