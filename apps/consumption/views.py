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

def consumo_page(request):

    clientes = Cliente.objects.all()

    if request.method == "POST":

        cliente_id = request.POST.get("cliente_id")
        mes = request.POST.get("mes") + "-01"
        consumo_kwh = request.POST.get("consumo_kwh")

        if not cliente_id or not mes or not consumo_kwh:
            return render(request, "consumo.html", {
                "erro": "Preencha todos os campos",
                "clientes": clientes
            })

        try:
            cliente = Cliente.objects.get(id=cliente_id)

            if Consumo.objects.filter(cliente=cliente, mes=mes).exists():
                return render(request, "consumo.html", {
                    "erro": "Consumo deste mês já cadastrado",
                    "clientes": clientes
                })

            Consumo.objects.create(
                cliente=cliente,
                mes=mes,
                consumo_kwh=consumo_kwh
            )

            return redirect("/dashboard/")

        except Cliente.DoesNotExist:
            return render(request, "consumo.html", {
                "erro": "Cliente não encontrado",
                "clientes": clientes
            })

    return render(request, "consumo.html", {"clientes": clientes})
