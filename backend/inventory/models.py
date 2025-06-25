from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# === Category Model ===
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    @classmethod
    def preload_defaults(cls):
        default_categories = [
            "Food", "Beverages", "Fruits", "Vegetables", "Frozen Foods",
            "Snacks", "Dairy", "Bakery", "Clothing", "Shoes", "Accessories",
            "Personal Care", "Pharmacy", "Electronics", "Hygiene",
            "Household Items", "Cleaning Supplies", "Kitchenware",
            "Stationery", "Toys", "Office Supplies", "Other"
        ]
        for name in default_categories:
            cls.objects.get_or_create(name=name)

    class Meta:
        ordering = ['name']

# === Item Model ===
class Item(models.Model):
    STATUS_CHOICES = (
        ('in_stock', 'In Stock'),
        ('running_low', 'Running Low'),
        ('out_of_stock', 'Out of Stock'),
    )

    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    quantity = models.PositiveIntegerField()
    date_added = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_stock')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return f"{self.name} - {self.quantity} ({self.get_status_display()})"

    def save(self, *args, **kwargs):
        self.update_status()
        super().save(*args, **kwargs)

    def update_status(self):
        if self.quantity == 0:
            self.status = 'out_of_stock'
        elif self.quantity <= 5:
            self.status = 'running_low'
        else:
            self.status = 'in_stock'

    class Meta:
        ordering = ['-date_added']

# === User Profile Model ===
class UserProfile(models.Model):
    ACCOUNT_TYPE_CHOICES = (
        ('personal', 'Personal'),
        ('business', 'Business'),
        ('admin', 'Admin'),
        ('staff', 'Staff'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=20)
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE_CHOICES)
    role = models.CharField(max_length=50, default='Manager')

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.account_type})"

    def get_full_name_or_username(self):
        return self.user.first_name or self.user.username
