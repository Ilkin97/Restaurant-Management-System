from rest_framework import serializers
from apps.menu.models import Category, Product, Favorite


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer to represent the Category model. This will handle
    serialization and deserialization of Category instances to and from JSON.
    """
    class Meta:
        model = Category
        fields = "__all__"  # Include all fields from the Category model


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer to represent the Product model. This will handle
    serialization and deserialization of Product instances to and from JSON.
    """
    class Meta:
        model = Product
        fields = "__all__"  # Include all fields from the Product model


class FavoriteSerializer(serializers.ModelSerializer):
    """
    Serializer to represent the Favorite model. This will handle
    serialization and deserialization of Favorite instances to and from JSON.
    """
    class Meta:
        model = Favorite
        fields = "__all__"  # Include all fields from the Favorite model
