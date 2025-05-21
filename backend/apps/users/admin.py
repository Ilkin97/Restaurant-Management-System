from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Fields to be displayed in the user list view
    list_display = ("email", "username", "role", "is_active", "is_staff", "is_superuser")
    # Filters available on the right side of the admin list view for easy searching
    list_filter = ("role", "is_active", "is_staff")
    # Fields to be searched in the admin list view
    search_fields = ("email", "username")
    # Default ordering of the users in the admin view (by email)
    ordering = ("email",)

    # Custom fields to display in the user detail page and form
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Fields", {"fields": ("role", "is_email_verified")}),  # Additional fields for role and email verification
    )
    
    # Fields to be used when adding a new user in the admin panel
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Fields", {"fields": ("role", "is_email_verified")}),  # Additional fields for adding a new user
    )

# Customizing the admin panel headers
admin.site.site_header = "Restaurant Management System"
admin.site.site_title = "Restaurant Management System"
admin.site.index_title = "Welcome to the Restaurant Management System"
