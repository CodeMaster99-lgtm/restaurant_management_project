from django.test import TestCase
from .models import Menu, Order

class MenuModelTest(testCase):
    def test_menu_creation(self):
        menu = Menu.objects.create(name='Test Menu', description='Test description', price=10.99)
        self.asserEqual(menu.name, 'Test Menu')

class OrderModelTest(TestCase):
    def test_order_creation(self):
        Order = Order.objects.create(customer=User.objects.create_user('testuser'), total_amount=10.99)
        self.asserEqual(order.total_amount,10.99)
