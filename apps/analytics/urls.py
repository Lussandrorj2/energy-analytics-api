from django.urls import path
from .views import (
    resumo_view,
    media_clientes_view,
    crescimento_view,
    anomalias_consumo_view,
    MediaConsumoView,
    crescimento_percentual_view,
    top_consumers_view
)

urlpatterns = [
    path("resumo-geral/", resumo_view, name="resumo-geral"),
    path("media-clientes/", media_clientes_view, name="media-clientes"),
    path("crescimento/", crescimento_view, name="crescimento"),
    path("anomalias/", anomalias_consumo_view, name="anomalias"),
    path("media-consumo/", MediaConsumoView.as_view(), name="media-consumo"),
    path("crescimento-percentual/", crescimento_percentual_view),
    path("top-consumers/", top_consumers_view, name="top-consumers"),
]