import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_clientes_requires_auth():
    client = APIClient()
    response = client.get("/api/v1/clientes/")
    assert response.status_code == 401


@pytest.mark.django_db
def test_clientes_with_token_returns_200():
    # cria usuário
    user = User.objects.create_user(
        username="testuser",
        password="testpass123"
    )

    client = APIClient()

    # obtém token JWT
    response = client.post(
        "/api/token/",
        {"username": "testuser", "password": "testpass123"},
        format="json"
    )

    access_token = response.data["access"]

    # envia token no header
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")

    response = client.get("/api/v1/clientes/")

    assert response.status_code == 200