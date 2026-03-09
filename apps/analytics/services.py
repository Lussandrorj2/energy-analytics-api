from django.db.models import Avg, Sum
from django.db.models.functions import TruncMonth
from apps.consumption.models import Consumo
from apps.users.models import Cliente
import statistics


# ================================
# 📊 RESUMO GERAL
# ================================
def resumo_geral(cliente_id=None):

    consumos = Consumo.objects.all()

    if cliente_id and cliente_id != "geral":
        consumos = consumos.filter(cliente_id=cliente_id)

    total_consumo = consumos.aggregate(
        total=Sum("consumo_kwh")
    )["total"] or 0

    media = consumos.aggregate(
        media=Avg("consumo_kwh")
    )["media"] or 0

    # contar TODOS os clientes cadastrados
    total_clientes = Cliente.objects.count()

    return {
        "total_consumo_geral": float(total_consumo),
        "media_geral": float(media),
        "total_clientes": total_clientes
    }


# ================================
# 📊 MÉDIA POR CLIENTE
# ================================
def media_por_cliente():

    clientes = (
        Cliente.objects
        .annotate(media=Avg("consumos__consumo_kwh"))
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

    if cliente_id and cliente_id != "geral":
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

    if cliente_id and cliente_id != "geral":
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
def detectar_anomalias(cliente_id):

    consumos = (
        Consumo.objects
        .filter(cliente_id=cliente_id)
        .order_by("mes")
    )

    if consumos.count() < 3:
        return []

    valores = [float(c.consumo_kwh) for c in consumos]

    media = statistics.mean(valores)
    desvio = statistics.stdev(valores)

    limite_superior = media + (2 * desvio)
    limite_inferior = media - (2 * desvio)

    anomalias = []

    for consumo in consumos:

        valor = float(consumo.consumo_kwh)

        if valor > limite_superior:

            anomalias.append({
                "cliente": consumo.cliente.nome,
                "mes": consumo.mes,
                "consumo_kwh": valor,
                "tipo": "alta"
            })

        elif valor < limite_inferior:

            anomalias.append({
                "cliente": consumo.cliente.nome,
                "mes": consumo.mes,
                "consumo_kwh": valor,
                "tipo": "baixa"
            })

    return anomalias


# ================================
# 📊 MÉDIA CONSUMO POR CLIENTE
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


# ================================
# 🏆 TOP CONSUMIDORES
# ================================
def top_consumers(limit=3):

    ranking = (
        Consumo.objects
        .values("cliente__nome")
        .annotate(consumo_total=Sum("consumo_kwh"))
        .order_by("-consumo_total")[:limit]
    )

    return list(ranking)


# ================================
# 📊 CONSUMO TOTAL POR CLIENTE
# ================================
def consumo_total_por_cliente():

    dados = (
        Consumo.objects
        .values("cliente__nome")
        .annotate(total=Sum("consumo_kwh"))
        .order_by("-total")
    )

    return list(dados)