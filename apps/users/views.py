from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from .models import Cliente
from .serializers import ClienteSerializer


class ClienteViewSet(ModelViewSet):

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['nome']