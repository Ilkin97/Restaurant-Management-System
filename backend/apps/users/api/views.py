from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import CustomUser
from .serializers import CustomUserSerializer
from ..permissions import IsAdmin, IsSuperAdmin, IsStaff


class CustomUserViewSet(viewsets.ModelViewSet):
    """
    Viewset to handle CRUD operations for all CustomUser objects.
    Only users with 'admin' permissions can access this viewset.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated, IsAdmin]  # Only admins can access this viewset


class SuperAdminViewSet(viewsets.ModelViewSet):
    """
    Viewset to handle CRUD operations for CustomUser objects with 'superadmin' role.
    Only users with 'superadmin' permissions can access this viewset.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated, IsSuperAdmin]  # Only superadmins can access this viewset


class StaffViewSet(viewsets.ModelViewSet):
    """
    Viewset to handle CRUD operations for CustomUser objects with 'staff' role.
    Only users with 'staff' permissions can access this viewset.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated, IsStaff]  # Only staff members can access this viewset


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, LoginSerializer


class RegisterView(APIView):
    """
    API view to handle user registration.
    This view is accessible to any user (no authentication required).
    """
    permission_classes = [AllowAny]

    def post(self, request):
        """
        Handles POST requests to register a new user.
        If the registration is successful, a message is returned.
        If not, validation errors are returned.
        """
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "Kayıt başarılı."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    """
    API view to handle user login and generate JWT tokens.
    This view is accessible to any user (no authentication required).
    """
    permission_classes = [AllowAny]

    def post(self, request):
        """
        Handles POST requests to login a user and return an access and refresh JWT token.
        """
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            refresh = RefreshToken.for_user(user)  # Generate a refresh token for the logged-in user
            return Response({
                "access": str(refresh.access_token),  # Access token for authenticated user
                "refresh": str(refresh),  # Refresh token for obtaining new access tokens
                "username": user.username,
                "email": user.email,
                "role": user.role  # User's role (e.g., admin, staff, etc.)
            })
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    """
    API view to handle user logout and blacklist refresh token.
    This view requires the user to be authenticated.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        Handles POST requests to logout a user by invalidating the refresh token.
        The refresh token is blacklisted, making it unusable for future authentication.
        """
        try:
            refresh_token = request.data["refresh"]  # Expecting the refresh token in the request body
            token = RefreshToken(refresh_token)  # Create a RefreshToken instance from the provided token
            token.blacklist()  # Blacklist the refresh token to prevent further usage
            return Response({"message": "Çıkış yapıldı."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response({"error": "Geçersiz token."}, status=status.HTTP_400_BAD_REQUEST)
