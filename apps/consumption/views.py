from rest_framework import viewsets
from django.shortcuts import render, redirect

from apps.users.models import Cliente
from .models import Consumo
from .serializers import ClienteSerializer, ConsumoSerializer


class ClienteViewSet(viewsets.ModelViewSet):

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    authentication_classes = []


class ConsumoViewSet(viewsets.ModelViewSet):

    queryset = Consumo.objects.all()
    serializer_class = ConsumoSerializer
    authentication_classes = []


def consumo_page(request):

    clientes = Cliente.objects.all()

    if request.method == "POST":

        cliente_id = request.POST.get("cliente_id")
        mes = request.POST.get("mes") + "-01"
        consumo_kwh = request.POST.get("consumo_kwh")

        cliente = Cliente.objects.get(id=cliente_id)

        Consumo.objects.create(
            cliente=cliente,
            mes=mes,
            consumo_kwh=consumo_kwh
        )

        return redirect("/dashboard/")

    return render(request, "consumo.html", {"clientes": clientes})