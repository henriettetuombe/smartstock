from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db.models import Q

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
