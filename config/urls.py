# config/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.consumption.views import ClienteViewSet, ConsumoViewSet,consumo_page
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.http import JsonResponse
from django.db import connection
from django.db.utils import OperationalError

# Import views from config
from .views import (
    home, health_check, dashboard, clientes_view, 
    analytics_page, top_consumidores_page, anomalias_page,
    login_view, logout_view
)

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'consumos', ConsumoViewSet)

urlpatterns = [
    # Root URL
    path("", home, name="home"),
    
    # Admin
    path('admin/', admin.site.urls),
    
    # Auth (Handled in config/views)
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    
    # Registration (Moved to apps/users)
    #path("", include("apps.users.urls")),
    
    # Protected Pages
    path("dashboard/", dashboard, name="dashboard"),
    path("clientes-view/", clientes_view, name="clientes"),
    #path("analytics/", analytics_page, name="analytics"),
    path("top-consumidores/", top_consumidores_page, name="top_consumidores_page"),
    path("anomalias/", anomalias_page, name="anomalias_page"),
    
    # Health Check
    path("health/", health_check, name="health"),
    
    # API Routes
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Versioned API
    path('api/v1/', include([
        path('', include(router.urls)),
        path('analytics/', include('apps.analytics.urls')),
    ])),
    
    # Consumption App URLs
    path('consumo/', include('apps.consumption.urls')),
]