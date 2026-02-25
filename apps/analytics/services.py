from .selectors import get_media_consumo_cliente
from apps.consumption.models import Consumo

def calcular_media_consumo(cliente_id:int):
    media = get_media_consumo_cliente(cliente_id)

    if media is None:
        return None
    
    Ultimo_consumo = (
        Consumo.objects
        .filter(cliente_id=cliente_id)
        .order_by("-mes")
        .first()
    )

    return {
        "cliente_id": cliente_id,
        "media": float(media),
        "ultimo_consumo": float(Ultimo_consumo.consumo_kwh) if Ultimo_consumo else None,
    }