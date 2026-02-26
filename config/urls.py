from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.consumption.views import ClienteViewSet, ConsumoViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.http import JsonResponse


def health_check(request):
    return JsonResponse({"status": "ok"})


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