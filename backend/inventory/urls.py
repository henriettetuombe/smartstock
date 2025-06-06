from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ItemViewSet,
    CategoryViewSet,
    current_user_view,
    get_auth_token,
    register_user
)

# === Register viewsets ===
router = DefaultRouter()
router.register(r'items', ItemViewSet, basename='item')
router.register(r'categories', CategoryViewSet, basename='category')

# === URL patterns ===
urlpatterns = [
    path('', include(router.urls)),                    # /api/items/, /api/categories/
    path('user/', current_user_view, name='user'),     # /api/user/
    path('token/', get_auth_token, name='get-token'),  # /api/token/
    path('register/', register_user, name='register'), # /api/register/
]
