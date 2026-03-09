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
from .views import home, health_check, dashboard, clientes_view, consumo, analytics_page,top_consumidores_page,anomalias_page
from .views import login_view, logout_view

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'consumos', ConsumoViewSet)


urlpatterns = [
    path("", home, name="home"),
    path("users/", include("apps.users.urls")),
    path("dashboard/", dashboard, name="dashboard"),
    path("clientes-view/", clientes_view, name="clientes"),
    path("analytics/", analytics_page, name="analytics"),
    path("consumo/", consumo, name="consumo"),
    path('admin/', admin.site.urls),
    path("health/", health_check, name="health"),
    path("top-consumidores/", top_consumidores_page, name="top_consumidores_page"),
    path("anomalias/", anomalias_page, name="anomalias_page"),
    path('', include('apps.consumption.urls')),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    
    # JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    
    
    # Versionamento
    path('api/v1/', include([
        path('', include(router.urls)),
        path('analytics/', include('apps.analytics.urls')),
    ])),
]