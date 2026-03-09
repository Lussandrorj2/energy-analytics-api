from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db import connection
from django.db.utils import OperationalError

from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from apps.consumption.models import Cliente
from apps.consumption.serializers import ClienteSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [AllowAny]


def home(request):
    return render(request, "home.html")


@login_required
def dashboard(request):
    return render(request, "dashboard.html")


@login_required
def clientes_view(request):
    return render(request, "clientes.html")


@login_required
def analytics_page(request):
    return render(request, "analytics.html")


@login_required
def consumo(request):
    return render(request, "consumo.html")


@login_required
def top_consumidores_page(request):
    return render(request, "top-consumidores.html")


@login_required
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


def login_view(request):

    if request.user.is_authenticated:
        return redirect("/dashboard/")

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)

            return redirect("/dashboard/")

        else:

            return render(request, "login.html", {
                "erro": "Usuário ou senha inválidos"
            })

    return render(request, "login.html")


@login_required
def logout_view(request):

    logout(request)

    return redirect("/login/")