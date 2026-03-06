from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.db.models import Avg, F, Q, Sum
from apps.consumption.models import Consumo
from apps.users.models import Cliente
from .services import (
    resumo_geral,
    media_por_cliente,
    crescimento_mensal,
    crescimento_percentual,
    detectar_anomalias,
    calcular_media_consumo,
    top_consumers,
    consumo_total_por_cliente,
)


# ================================
# 📊 RESUMO GERAL
# ================================
@api_view(["GET"])
@permission_classes([AllowAny])
def resumo_view(request):
    cliente_id = request.GET.get("cliente")
    return Response(resumo_geral(cliente_id))


# ================================
# 📊 MÉDIA POR CLIENTE
# ================================
@api_view(["GET"])
@permission_classes([AllowAny])
def media_clientes_view(request):
    return Response(media_por_cliente())


# ================================
# 📈 CRESCIMENTO MENSAL (GRÁFICO)
# ================================
@api_view(["GET"])
@permission_classes([AllowAny])
def crescimento_view(request):
    cliente_id = request.GET.get("cliente_id")

    if not cliente_id:
        return Response(
            {"error": "cliente_id obrigatório"},
            status=status.HTTP_400_BAD_REQUEST
        )

    if cliente_id == "geral":
        data = crescimento_mensal(None)
    else:
        try:
            cliente_id = int(cliente_id)
        except ValueError:
            return Response(
                {"error": "cliente_id inválido"},
                status=status.HTTP_400_BAD_REQUEST
            )

        data = crescimento_mensal(cliente_id)

    if not data:
        return Response(
            {"error": "Dados insuficientes"},
            status=status.HTTP_404_NOT_FOUND
        )

    return Response(data)


# ================================
# 📈 CRESCIMENTO PERCENTUAL
# ================================
@api_view(["GET"])
@permission_classes([AllowAny])
def crescimento_percentual_view(request):
    cliente_id = request.GET.get("cliente_id")

    if not cliente_id:
        return Response(
            {"error": "cliente_id obrigatório"},
            status=status.HTTP_400_BAD_REQUEST
        )

    if cliente_id == "geral":
        data = crescimento_percentual(None)
    else:
        try:
            cliente_id = int(cliente_id)
        except ValueError:
            return Response(
                {"error": "cliente_id inválido"},
                status=status.HTTP_400_BAD_REQUEST
            )

        data = crescimento_percentual(cliente_id)

    if not data:
        return Response(
            {"error": "Dados insuficientes"},
            status=status.HTTP_404_NOT_FOUND
        )

    return Response(data)


# ================================
# 🚨 DETECTAR ANOMALIAS
# ================================

@api_view(["GET"])
@permission_classes([AllowAny])
def anomalias_consumo_view(request):

    media = Consumo.objects.aggregate(
        media=Avg("consumo_kwh")
    )["media"]

    if not media:
        return Response([])

    anomalias = (
        Consumo.objects
        .filter(consumo_kwh__gt=media * 2)
        .values("cliente__nome","consumo_kwh")
    )

    return Response(list(anomalias))


# ================================
# 📊 MÉDIA CONSUMO DETALHADA
# ================================

class MediaConsumoView(APIView):

    def get(self, request):
        cliente_id = request.query_params.get("cliente_id")

        if not cliente_id:
            return Response(
                {"error": "cliente_id é obrigatório"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            cliente_id = int(cliente_id)
        except ValueError:
            return Response(
                {"error": "cliente_id deve ser inteiro"},
                status=status.HTTP_400_BAD_REQUEST
            )

        data = calcular_media_consumo(cliente_id)

        if data is None:
            return Response(
                {"error": "Cliente não possui consumos"},
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(data)
    
    
#===========================
# 🏆 TOP CONSUMIDORES
#===========================

@api_view(["GET"])
@permission_classes([AllowAny])
def top_consumers_view(request):

    limit = request.GET.get("limit", 3)

    data = top_consumers(int(limit))

    return Response(data)


@api_view(["GET"])
def buscar_clientes(request):

    nome = request.GET.get("nome", "")

    clientes = Cliente.objects.filter(
        nome__icontains=nome
    ).values("id", "nome", "documento")[:20]

    return Response(list(clientes))

@api_view(["GET"])
@permission_classes([AllowAny])
def consumo_clientes_view(request):

    data = consumo_total_por_cliente()

    return Response(data)


@api_view(["GET"])
@permission_classes([AllowAny])
def consumo_total_cliente_view(request):

    data = (
        Consumo.objects
        .values("cliente__nome")
        .annotate(total=Sum("consumo_kwh"))
        .order_by("-total")[:10]
    )

    labels = []
    valores = []

    for item in data:
        labels.append(item["cliente__nome"])
        valores.append(float(item["total"] or 0))

    return Response({
        "labels": labels,
        "valores": valores
    })