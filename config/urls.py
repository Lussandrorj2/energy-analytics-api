from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.consumption.views import ClienteViewSet, ConsumoViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.http import JsonResponse


from django.http import JsonResponse
from django.db import connection
from django.db.utils import OperationalError


def health_check(request):
    try:
        connection.ensure_connection()
        return JsonResponse({
            "status": "ok",
            "database": "connected"
        })
    except OperationalError:
        return JsonResponse({
            "status": "error",
            "database": "disconnected"
        }, status=500)


router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'consumos', ConsumoViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("health/", health_check),

    # JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Versionamento
    path('api/v1/', include([
        path('', include(router.urls)),
        path('analytics/', include('apps.analytics.urls')),
    ])),
]