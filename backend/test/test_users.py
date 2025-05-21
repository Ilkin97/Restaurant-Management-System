from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model


class UserTests(APITestCase):

    def setUp(self):
        """Set up the necessary test users."""
        self.superadmin = get_user_model().objects.create_user(
            email="superadmin@example.com",
            username="superadmin",
            password="superadminpassword",
            role="SUPERADMIN",
            is_email_verified=True
        )
        self.admin = get_user_model().objects.create_user(
            email="admin@example.com",
            username="admin",
            password="adminpassword",
            role="ADMIN",
            is_email_verified=True
        )
        self.staff = get_user_model().objects.create_user(
            email="staff@example.com",
            username="staff",
            password="staffpassword",
            role="STAFF",
            is_email_verified=True
        )
        self.customer = get_user_model().objects.create_user(
            email="customer@example.com",
            username="customer",
            password="customerpassword",
            role="CUSTOMER",
            is_email_verified=True
        )

    def test_create_user(self):
        """Test user creation and response."""
        response = self.client.post('/api/users/register/', {
            'email': 'testuser@example.com',
            'username': 'testuser',
            'password': 'testpassword',
            'role': 'CUSTOMER'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login_user(self):
        """Test user login and token generation."""
        response = self.client.post('/api/users/login/', {
            'email': 'superadmin@example.com',
            'password': 'superadminpassword',
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_login_invalid_user(self):
        """Test login with invalid credentials."""
        response = self.client.post('/api/users/login/', {
            'email': 'invaliduser@example.com',
            'password': 'wrongpassword',
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_permissions_for_admin(self):
        """Test that only admin users can access certain endpoints."""
        self.client.force_authenticate(user=self.admin)
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_permissions_for_non_admin(self):
        """Test that non-admin users can't access admin endpoints."""
        self.client.force_authenticate(user=self.customer)
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_logout_user(self):
        """Test user logout and token blacklisting."""
        # Get the refresh token for logout
        response = self.client.post('/api/users/login/', {
            'email': 'superadmin@example.com',
            'password': 'superadminpassword',
        })
        refresh_token = response.data['refresh']
        
        response = self.client.post('/api/users/logout/', {'refresh': refresh_token})
        self.assertEqual(response.status_code, status.HTTP_205_RESET_CONTENT)
