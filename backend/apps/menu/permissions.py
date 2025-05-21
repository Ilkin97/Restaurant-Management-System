from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    """
    Custom permission to grant access only to users with an 'ADMIN' role.

    This permission checks if the user is authenticated and whether their
    role is 'ADMIN'. It is typically used for restricting access to 
    administrative views in the application.
    """
    
    def has_permission(self, request, view):
        """
        Check if the user has the 'ADMIN' role.

        Args:
            request: The HTTP request object.
            view: The view that is being accessed.

        Returns:
            bool: True if the user is authenticated and has the 'ADMIN' role, 
                  False otherwise.
        """
        return request.user.is_authenticated and request.user.role == "ADMIN"
