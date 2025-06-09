from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from apps.menu.models import Category, Product, Favorite
from .serializers import CategorySerializer, ProductSerializer, FavoriteSerializer
from apps.menu.permissions import IsAdmin


# View for listing all categories.
# It retrieves all the Category objects and returns them as a list using the CategorySerializer.
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()  # Fetch all categories
    serializer_class = CategorySerializer  # Use CategorySerializer to format the response


# View for listing all products.
# It retrieves all the Product objects and returns them as a list using the ProductSerializer.
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()  # Fetch all products
    serializer_class = ProductSerializer  # Use ProductSerializer to format the response


# View for adding a product to the user's favorites.
# It allows authenticated users to add products to their favorite list.
class AddToFavoriteView(generics.CreateAPIView):
    queryset = Favorite.objects.all()  # Fetch all favorite objects
    serializer_class = FavoriteSerializer  # Use FavoriteSerializer to format the request and response
    permission_classes = [IsAuthenticated]  # Only authenticated users can add to favorites

    # Override the perform_create method to automatically assign the current user to the favorite item.
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Save the favorite with the current user


# View for listing all favorite items of the authenticated user.
# It fetches only the favorites related to the current logged-in user.
class FavoriteListView(generics.ListAPIView):
    serializer_class = FavoriteSerializer  # Use FavoriteSerializer to format the response

    # Override the get_queryset method to filter favorites by the current user.
    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)  # Fetch only the favorites for the current user


# Admin view for creating a new product.
# Only users with the IsAdmin permission can create new products.
class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()  # Fetch all product objects
    serializer_class = ProductSerializer  # Use ProductSerializer to format the request and response
    permission_classes = [IsAdmin]  # Only admin users can create new products


# Admin view for updating an existing product.
# Only users with the IsAdmin permission can update products.
class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()  # Fetch all product objects
    serializer_class = ProductSerializer  # Use ProductSerializer to format the request and response
    permission_classes = [IsAdmin]  # Only admin users can update products


# Admin view for deleting an existing product.
# Only users with the IsAdmin permission can delete products.
class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()  # Fetch all product objects
    permission_classes = [IsAdmin]  # Only admin users can delete products
