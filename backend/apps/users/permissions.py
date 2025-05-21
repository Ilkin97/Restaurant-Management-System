from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    """
    Custom permission class to check if the user has 'ADMIN' role
    or if the user is a superuser.
    """
    def has_permission(self, request, view):
        """
        Check if the user has permission to access the resource.
        The user must be authenticated and have 'ADMIN' role or be a superuser.
        """
        return request.user.is_authenticated and (
            request.user.role == "ADMIN" or request.user.is_superuser
        )


class IsSuperAdmin(BasePermission):
    """
    Custom permission class to check if the user has 'SUPERADMIN' role
    or if the user is a superuser.
    """
    def has_permission(self, request, view):
        """
        Check if the user has permission to access the resource.
        The user must be authenticated and have 'SUPERADMIN' role or be a superuser.
        """
        return request.user.is_authenticated and (
            request.user.role == "SUPERADMIN" or request.user.is_superuser
        )


class IsStaff(BasePermission):
    """
    Custom permission class to check if the user has 'STAFF' role
    or if the user is a staff member.
    """
    def has_permission(self, request, view):
        """
        Check if the user has permission to access the resource.
        The user must be authenticated and have 'STAFF' role or be a staff member.
        """
        return request.user.is_authenticated and (
            request.user.role == "STAFF" or request.user.is_staff
        )
