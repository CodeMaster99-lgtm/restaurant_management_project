from django.test import TestCase, Client
from .models import MenuItem
from django.urls import reverse

class MenuItemModelsTest(TestCase):
    def test_create_menu_item(self):
        self = MenuItem.objects.create(name='Test Pizza', price=199.99)
        self.assertEqual(item.name, "Test Pizza")
        self.assertEqual(item.price, 199.99)

class MenuItemAPITest(TestCase):
    def setUp(self):
        MenuItem.objects.create(name="Burger",price=120)
        MenuItem.objects.create(name="Pasta", price=180)

    def test_menu_api_returns_json(self):
        client = Client()
        response = client.get(reverse('menu-api'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-Type'], 'application/json')

        data = response.json()
        self.assertIsInstance(data,list)
        self.assertEqual(len(data),2)
        self.assertEqual(data[0]['name'],"Burger")
        self.assertEqual(data[1]['name'],"Pasta")

