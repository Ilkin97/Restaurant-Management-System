"""
URL configuration for the core project.

The `urlpatterns` list routes URLs to views. For more information, please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/

Examples:
Function views:
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')

Class-based views:
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')

Including another URLconf:
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    # Admin panel
    # This path routes the admin panel of the project.
    path('admin/', admin.site.urls),

    # Users app
    # This path includes all the URL patterns for the 'users' app in the project.
    path('api/users/', include('apps.users.api.urls')),

    # Menu app
    # This path includes all the URL patterns for the 'menu' app.
    path('api/menu/', include('apps.menu.api.urls')),

    # Orders app
    # This path includes all the URL patterns for the 'orders' app.
    path('api/orders/', include('apps.orders.api.urls')),

    # Inventory app
    # This path includes all the URL patterns for the 'inventory' app.
    path('api/inventory/', include('apps.inventory.api.urls')),

    # Feedback app
    # This path includes all the URL patterns for the 'feedback' app.
    path('api/feedback/', include('apps.feedback.api.urls')),

    # Reports app
    # This path includes all the URL patterns for the 'reports' app.
    path('api/reports/', include('apps.reports.api.urls')),

    # Ads app
    # This path includes all the URL patterns for the 'ads' app.
    path('api/ads/', include('apps.ads.api.urls')),
]

# Serve static files in development mode
# This block adds media file routing only if Django is in DEBUG mode.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
