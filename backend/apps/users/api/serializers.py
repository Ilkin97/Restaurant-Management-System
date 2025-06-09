from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from apps.users.models import CustomUser

# Get the CustomUser model, which may be customized
CustomUser = get_user_model()  # This will use the custom user model defined in the project settings


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer for CustomUser model. It handles user data including password hashing
    during user creation and updating.
    """
    password = serializers.CharField(write_only=True)  # Password is write-only for security purposes

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'role', 'password')  # Fields to be included in the serialized data

    def create(self, validated_data):
        """
        Create a new CustomUser with the given validated data.
        Hashes the password before saving the user to the database.
        """
        password = validated_data.pop('password')  # Extract password from validated data to hash it
        user = CustomUser.objects.create_user(**validated_data)  # Use create_user method to hash password
        user.set_password(password)  # Ensure the password is hashed correctly
        user.save()  # Save the user instance to the database
        return user

    def update(self, instance, validated_data):
        """
        Update an existing CustomUser instance with new validated data.
        If a password is provided, it will be hashed and updated as well.
        """
        password = validated_data.pop('password', None)  # Pop password if provided, it’s optional
        for attr, value in validated_data.items():
            setattr(instance, attr, value)  # Update the instance attributes with the validated data
        if password:
            instance.set_password(password)  # Hash the new password before saving it
        instance.save()  # Save the updated instance to the database
        return instance


class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for registering a new CustomUser. This serializer allows users to register
    by providing their username, email, and password. The password is hashed before saving.
    """
    password = serializers.CharField(write_only=True)  # Password is write-only for security

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password", "role")  # Fields required for registration

    def create(self, validated_data):
        """
        Creates a new user instance and hashes the password before saving the user.
        Sets the role to CUSTOMER by default if not provided.
        """
        user = CustomUser.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            role=validated_data.get("role", CustomUser.Role.CUSTOMER),  # Default role is CUSTOMER
        )
        return user


class LoginSerializer(serializers.Serializer):
    """
    Serializer for user login. It validates the provided email and password for authentication.
    If the user is valid and active, it returns the user instance.
    """
    email = serializers.EmailField()  # Email field for login
    password = serializers.CharField()  # Password field for login

    def validate(self, data):
        """
        Validates the login credentials (email and password).
        Authenticates the user and ensures the user is active.
        """
        user = authenticate(email=data["email"], password=data["password"])  # Authenticate the user
        if not user:
            raise serializers.ValidationError("Invalid email or password.")  # Raise error if user not found
        if not user.is_active:
            raise serializers.ValidationError("User is inactive.")  # Raise error if user is inactive
        data["user"] = user  # Add the authenticated user to the data
        return data
