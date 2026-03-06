from django.db.models import Avg, Sum
from django.db.models.functions import TruncMonth
from apps.consumption.models import Cliente, Consumo
import statistics
from rest_framework.decorators import api_view
from rest_framework.response import Response


# ================================
# 📊 RESUMO GERAL
# ================================
def resumo_geral(cliente_id=None):

    consumos = Consumo.objects.all()

    if cliente_id and cliente_id != "geral":
        consumos = consumos.filter(cliente_id=cliente_id)

    total_consumo = consumos.aggregate(
        total=Sum("consumo_kwh")
    )["total"]

    media = consumos.aggregate(
        media=Avg("consumo_kwh")
    )["media"]

    total_clientes = consumos.values("cliente").distinct().count()

    return {
        "total_consumo_geral": total_consumo or 0,
        "media_geral": media or 0,
        "total_clientes": total_clientes
    }


# ================================
# 📊 MÉDIA POR CLIENTE
# ================================
def media_por_cliente():
    clientes = (
        Cliente.objects
        .annotate(media=Avg("consumo__consumo_kwh"))
        .values("id", "nome", "media")
    )

    return [
        {
            "cliente_id": c["id"],
            "cliente_nome": c["nome"],
            "media": round(float(c["media"] or 0), 2)
        }
        for c in clientes
    ]


# ================================
# 📈 CRESCIMENTO MENSAL (GRÁFICO)
# ================================
def crescimento_mensal(cliente_id=None):
    queryset = Consumo.objects.all()

    if cliente_id:
        queryset = queryset.filter(cliente_id=cliente_id)

    consumos = (
        queryset
        .annotate(mes_truncado=TruncMonth("mes"))
        .values("mes_truncado")
        .annotate(total=Sum("consumo_kwh"))
        .order_by("mes_truncado")
    )

    resultado = []

    for item in consumos:
        resultado.append({
            "mes": item["mes_truncado"].strftime("%m/%Y"),
            "consumo": float(item["total"] or 0)
        })

    return resultado


# ================================
# 📈 CRESCIMENTO PERCENTUAL
# ================================
def crescimento_percentual(cliente_id=None):
    queryset = Consumo.objects.all()

    if cliente_id:
        queryset = queryset.filter(cliente_id=cliente_id)

    consumos = queryset.order_by("-mes")

    if consumos.count() < 2:
        return None

    atual = float(consumos[0].consumo_kwh)
    anterior = float(consumos[1].consumo_kwh)

    if anterior == 0:
        return None

    crescimento = ((atual - anterior) / anterior) * 100

    return {
        "mes_atual": atual,
        "mes_anterior": anterior,
        "crescimento_percentual": round(crescimento, 2)
    }


# ================================
# 🚨 DETECTAR ANOMALIAS
# ================================
def detectar_anomalias(cliente_id: int):

    consumos = (
        Consumo.objects
        .filter(cliente_id=cliente_id)
        .order_by("mes")
        .values_list("consumo_kwh", flat=True)
    )

    consumos = list(consumos)

    if len(consumos) < 3:
        return []

    media = statistics.mean(consumos)
    desvio = statistics.stdev(consumos)

    limite_superior = media + (2 * desvio)
    limite_inferior = media - (2 * desvio)

    dados = (
        Consumo.objects
        .filter(cliente_id=cliente_id)
        .order_by("mes")
    )

    anomalias = []

    for item in dados:

        if item.consumo_kwh > limite_superior:
            anomalias.append({
                "mes": item.mes,
                "consumo": item.consumo_kwh,
                "tipo": "alta"
            })

        elif item.consumo_kwh < limite_inferior:
            anomalias.append({
                "mes": item.mes,
                "consumo": item.consumo_kwh,
                "tipo": "baixa"
            })

    return {
        "media": None,
        "limite_superior": None,
        "limite_inferior": None,
        "anomalias": []
    }


# ================================
# 📊 MÉDIA CONSUMO POR CLIENTE (DETALHADO)
# ================================
def calcular_media_consumo(cliente_id):
    media = (
        Consumo.objects
        .filter(cliente_id=cliente_id)
        .aggregate(media=Avg("consumo_kwh"))
    )["media"]

    if not media:
        return None

    ultimo_consumo = (
        Consumo.objects
        .filter(cliente_id=cliente_id)
        .order_by("-mes")
        .values_list("consumo_kwh", flat=True)
        .first()
    )

    return {
        "cliente_id": cliente_id,
        "media": round(float(media), 2),
        "ultimo_consumo": float(ultimo_consumo or 0),
    }

#===========================
# 🏆 TOP CONSUMIDORES
#===========================

def top_consumers(limit=3):

    ranking = (
        Consumo.objects
        .values("cliente__nome")
        .annotate(consumo_total=Sum("consumo_kwh"))
        .order_by("-consumo_total")[:limit]
    )

    return list(ranking)