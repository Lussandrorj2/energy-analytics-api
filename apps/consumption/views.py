from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from django.shortcuts import render, redirect

from .models import Cliente, Consumo
from .serializers import ClienteSerializer, ConsumoSerializer


# ================================
# API CLIENTES
# ================================

class ClienteViewSet(viewsets.ModelViewSet):

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [AllowAny]
    authentication_classes = []


# ================================
# API CONSUMO
# ================================

class ConsumoViewSet(viewsets.ModelViewSet):

    queryset = Consumo.objects.all()
    serializer_class = ConsumoSerializer
    permission_classes = [AllowAny]
    authentication_classes = []


# ================================
# PÁGINA HTML REGISTRAR CONSUMO
# ================================

from django.shortcuts import render, redirect
from .models import Cliente, Consumo


def consumo_page(request):

    if request.method == "POST":

        cliente_id = request.POST.get("cliente_id")
        mes = request.POST.get("mes")
        consumo_kwh = request.POST.get("consumo_kwh")

        try:
            cliente = Cliente.objects.get(id=cliente_id)

            Consumo.objects.create(
                cliente=cliente,
                mes=mes,
                consumo_kwh=consumo_kwh
            )

        except Cliente.DoesNotExist:
            print("Cliente não encontrado")

        return redirect("/consumo/")

    return render(request, "consumo.html")
