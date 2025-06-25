from django.test import TestCase
from django.contrib.auth.models import User
from .models import Item, Category

class ItemModelTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create a test category
        self.category = Category.objects.create(name='Food')

        # Create an item
        self.item = Item.objects.create(
            name="Milk",
            category=self.category,
            quantity=10,
            owner=self.user
        )

    def test_item_creation(self):
        item = Item.objects.get(name="Milk")
        self.assertEqual(item.quantity, 10)
        self.assertEqual(item.category.name, "Food")
        self.assertEqual(item.owner.username, "testuser")
        self.assertIn(item.status, ["in_stock", "low_stock", "out_of_stock"])  # Based on update_status logic
