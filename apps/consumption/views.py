from rest_framework import viewsets
from .models import Cliente, Consumo
from .serializers import ClienteSerializer, ConsumoSerializer
from rest_framework.permissions import AllowAny
from rest_framework.authentication import SessionAuthentication
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [AllowAny]
    authentication_classes = []
class ConsumoViewSet(viewsets.ModelViewSet):
    queryset = Consumo.objects.all()
    serializer_class = ConsumoSerializer
    permission_classes = [AllowAny]
    authentication_classes = []
