from rest_framework.test import APITestCase
from rest_framework import status

class OrderTests(APITestCase):

    def test_create_order(self):
        """Test creating a new order."""
        data = {'user': 1, 'item': 1, 'quantity': 2}
        response = self.client.post('/api/orders/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_orders(self):
        """Test retrieving orders."""
        response = self.client.get('/api/orders/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
