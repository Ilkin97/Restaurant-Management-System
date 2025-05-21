from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    # A field to store email verification status
    is_email_verified = models.BooleanField(default=False)

    # Enum-like class for user roles
    class Role(models.TextChoices):
        CUSTOMER = "CUSTOMER", _("Customer")
        STAFF = "STAFF", _("Staff")
        ADMIN = "ADMIN", _("Admin")
        SUPERADMIN = "SUPERADMIN", _("Super Admin")

    # User role field with choices for better classification
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.CUSTOMER,
        verbose_name="User Role"
    )

    # The email field that uniquely identifies a user
    email = models.EmailField(unique=True, verbose_name="Email")
    
    # A field for email verification status
    is_email_verified = models.BooleanField(default=False, verbose_name="Is Email Verified?")

    # Setting email as the username for the authentication process
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        # Return a string representation of the user with username and role
        return f"{self.username} ({self.role})"

    def is_admin(self):
        # Check if the user has admin privileges
        return self.role == self.Role.ADMIN or self.is_superuser

    def is_staff_member(self):
        # Check if the user is a staff member
        return self.role == self.Role.STAFF or self.is_staff

    def is_super_admin(self):
        # Check if the user is a super admin
        return self.role == self.Role.SUPERADMIN or self.is_superuser
