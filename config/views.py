from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
from django.db.utils import OperationalError

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