from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
from django.db.utils import OperationalError
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from apps.consumption.models import Cliente
from apps.consumption.serializers import ClienteSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [AllowAny]

def home(request):
    return render(request, "home.html")

def dashboard(request):
    return render(request, "dashboard.html")

def clientes_view(request):
    return render(request, "clientes.html")

def analytics_page(request):
    return render(request, "analytics.html")

def consumo(request):
    return render(request, "consumo.html")

def top_consumidores_page(request):
    return render(request, "top-consumidores.html")

def anomalias_page(request):
    return render(request, "anomalias.html")

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