from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db.models import Q
from django.http import HttpResponse
from django.contrib.auth import get_user_model

from .models import Category, Item
from .serializers import (
    CategorySerializer,
    ItemSerializer,
    UserSerializer,
    UserRegistrationSerializer
)

# === Category API ===
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

# === Item API ===
class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Item.objects.filter(owner=self.request.user).order_by('-date_added')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)

# === Get Logged-In User Info ===
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user_view(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

# === JWT Authentication Login (by email or username) ===
@api_view(['POST'])
@permission_classes([AllowAny])
def get_auth_token(request):
    """
    Accepts: { "username": "email or username", "password": "yourpassword" }
    Returns: { "refresh": "...", "access": "..." }
    """
    identifier = request.data.get('username')
    password = request.data.get('password')

    if not identifier or not password:
        return Response({"error": "Username/email and password are required."},
                        status=status.HTTP_400_BAD_REQUEST)

    users = User.objects.filter(Q(username=identifier) | Q(email=identifier))

    if users.count() != 1:
        return Response({"error": "Invalid or duplicate credentials."},
                        status=status.HTTP_401_UNAUTHORIZED)

    user_obj = users.first()
    user = authenticate(username=user_obj.username, password=password)

    if user:
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        })

    return Response({"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)

# === User Registration ===
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    """
    Accepts: first_name, last_name, email, phone_number,
             account_type, password, confirm_password
    Returns: access & refresh tokens or validation errors
    """
    serializer = UserRegistrationSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            "message": "User registered successfully.",
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# === Temporary Admin Creation View (for Render deployment) ===
@api_view(['GET'])
@permission_classes([AllowAny])
def create_admin_user(request):
    """
    Temporary view to create a superuser on Render where shell access isn't available.
    Visit /create-admin/ ONCE after deploy, then delete this view from production.
    """
    User = get_user_model()
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='admin@gmail.com',
            password='AdminPassword123'  #  Change to something strong
        )
        return HttpResponse(" Superuser 'admin' created successfully.")
    return HttpResponse(" Superuser already exists.")

# === One-time Category Seeder (Call /seed-categories/ after deploy) ===
@api_view(['GET'])
@permission_classes([AllowAny])
def seed_categories(request):
    """
    Seeds 25 default categories. Call once via /seed-categories/ then remove this.
    """
    default_categories = [
        "Electronics", "Clothing", "Shoes", "Bakery", "Dairy",
        "Frozen Foods", "Hygiene", "Beverages", "Toys", "Accessories",
        "Books", "Stationery", "Pet Supplies", "Cleaning Supplies", "Beauty",
        "Furniture", "Sports Equipment", "Gardening", "Automotive", "Baby Products",
        "Office Supplies", "Health", "Groceries", "Music", "Games"
    ]
    created = []
    for name in default_categories:
        obj, was_created = Category.objects.get_or_create(name=name)
        if was_created:
            created.append(name)
    if created:
        return Response({"message": f"Categories added: {', '.join(created)}"})
    return Response({"message": "All default categories already exist."})
