from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ItemViewSet,
    CategoryViewSet,
    current_user_view,
    get_auth_token,
    register_user,
    create_admin_user,     # ✅ Existing temporary admin view
    seed_categories        # ✅ Newly added category seeder
)

# === Register viewsets ===
router = DefaultRouter()
router.register(r'items', ItemViewSet, basename='item')
router.register(r'categories', CategoryViewSet, basename='category')

# === URL patterns ===
urlpatterns = [
    path('', include(router.urls)),                      # /api/items/, /api/categories/
    path('user/', current_user_view, name='user-info'),  # GET: /api/user/
    path('token/', get_auth_token, name='get-token'),    # POST: /api/token/
    path('register/', register_user, name='register'),   # POST: /api/register/
    path('create-admin/', create_admin_user),            # ✅ TEMP: /api/create-admin/
    path('seed-categories/', seed_categories),           # ✅ TEMP: /api/seed-categories/
]
