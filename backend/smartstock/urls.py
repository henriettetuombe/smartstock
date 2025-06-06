from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.http import JsonResponse

def home_view(request):
    return JsonResponse({
        "status": "success",
        "message": "Welcome to the SmartStock API",
        "available_endpoints": {
            "Admin Panel": "/admin/",
            "Inventory API": {
                "Categories": "/api/categories/",
                "Items": "/api/items/",
                "User Info": "/api/user/"
            },
            "Authentication": {
                "Login": "/api/token/",
                "Refresh": "/api/token/refresh/"
            }
        }
    }, status=200)

urlpatterns = [
    path('', home_view, name='api-root'),
    path('admin/', admin.site.urls),
    path('api/', include('inventory.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include('rest_framework.urls')),  # Optional: DRF browsable login
]
