from django.urls import path
from . import views

urlpatterns = [
    # URL route for listing all categories.
    # When a GET request is made to 'categories/', the CategoryListView will be triggered
    # to return a list of all categories.
    path("categories/", views.CategoryListView.as_view(), name="category-list"),

    # URL route for listing all products.
    # When a GET request is made to 'products/', the ProductListView will be triggered
    # to return a list of all available products.
    path("products/", views.ProductListView.as_view(), name="product-list"),

    # URL route for listing all favorite items.
    # When a GET request is made to 'favorites/', the FavoriteListView will be triggered
    # to return a list of all user favorite items.
    path("favorites/", views.FavoriteListView.as_view(), name="favorite-list"),

    # URL route for adding a product to favorites.
    # When a POST request is made to 'favorites/add/', the AddToFavoriteView will be triggered
    # to handle the process of adding a product to the user's favorite list.
    path("favorites/add/", views.AddToFavoriteView.as_view(), name="add-to-favorite"),
    
    # Admin routes for managing products.
    
    # URL for creating a new product.
    # When a POST request is made to 'admin/products/create/', the ProductCreateView will be triggered
    # to handle the creation of a new product by the admin.
    path("admin/products/create/", views.ProductCreateView.as_view(), name="product-create"),

    # URL for updating an existing product by its primary key (pk).
    # When a PUT or PATCH request is made to 'admin/products/<int:pk>/update/', the ProductUpdateView will be triggered
    # to handle the update of the specific product identified by pk.
    path("admin/products/<int:pk>/update/", views.ProductUpdateView.as_view(), name="product-update"),

    # URL for deleting a product by its primary key (pk).
    # When a DELETE request is made to 'admin/products/<int:pk>/delete/', the ProductDeleteView will be triggered
    # to handle the deletion of the specific product identified by pk.
    path("admin/products/<int:pk>/delete/", views.ProductDeleteView.as_view(), name="product-delete"),
]
