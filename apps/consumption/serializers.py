from rest_framework import serializers
from .models import Cliente, Consumo

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class ConsumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumo
        fields = '__all__'