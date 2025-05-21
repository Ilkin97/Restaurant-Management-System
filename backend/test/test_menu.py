from rest_framework.test import APITestCase
from rest_framework import status

class MenuTests(APITestCase):

    def test_get_menu(self):
        """Test the menu API endpoint."""
        response = self.client.get('/api/menu/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_menu_item(self):
        """Test creating a new menu item."""
        data = {'name': 'Pizza', 'price': 15.99}
        response = self.client.post('/api/menu/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_menu_item(self):
        """Test updating an existing menu item."""
        # Assume we already have a menu item with ID 1
        response = self.client.put('/api/menu/1/', {'name': 'Burger', 'price': 12.99})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_menu_item(self):
        """Test deleting a menu item."""
        # Assume we already have a menu item with ID 1
        response = self.client.delete('/api/menu/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
