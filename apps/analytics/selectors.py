from django.db.models import Avg
from apps.consumption.models import Consumo

def get_media_consumo_cliente(cliente_id: int):
    return (
        Consumo.objects
        .filter(cliente_id=cliente_id)
        .aggregate(media=Avg("consumo_kwh"))
    )["media"]