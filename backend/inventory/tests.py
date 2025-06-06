from django.test import TestCase
from .models import Item

class ItemModelTest(TestCase):
    def setUp(self):
        Item.objects.create(name="Milk", category="Food", quantity=10, status="in_stock")

    def test_item_creation(self):
        item = Item.objects.get(name="Milk")
        self.assertEqual(item.quantity, 10)
