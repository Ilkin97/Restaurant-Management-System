from rest_framework.test import APITestCase
from rest_framework import status

class InventoryTests(APITestCase):

    def test_add_item_to_inventory(self):
        """Test adding an item to the inventory."""
        data = {'name': 'Tomato', 'quantity': 50}
        response = self.client.post('/api/inventory/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_inventory(self):
        """Test retrieving inventory."""
        response = self.client.get('/api/inventory/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
