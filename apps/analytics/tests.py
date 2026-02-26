import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from apps.consumption.models import Cliente, Consumo


@pytest.mark.django_db
def test_media_consumo_endpoint():
    client = APIClient()

    # Criar usuário
    user = User.objects.create_user(
        username="testuser",
        password="123456"
    )

    # Obter token JWT
    response = client.post("/api/token/", {
        "username": "testuser",
        "password": "123456"
    })

    assert response.status_code == 200
    token = response.data["access"]

    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    # Criar cliente
    cliente = Cliente.objects.create(
        nome="Cliente Teste",
        documento="12345678900"
    )

    # Criar consumos
    Consumo.objects.create(
        cliente=cliente,
        mes="2026-01-01",
        consumo_kwh=300
    )

    Consumo.objects.create(
        cliente=cliente,
        mes="2026-02-01",
        consumo_kwh=400
    )

    # Testar endpoint de média
    response = client.get(
        f"/api/v1/analytics/media-consumo/?cliente_id={cliente.id}"
    )

    assert response.status_code == 200
    assert response.data["cliente_id"] == cliente.id
    assert response.data["media"] == 350