from rest_framework import serializers
from .models import Cliente, Consumo

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class ConsumoSerializer(serializers.ModelSerializer):
    # Cria campos amigáveis para o Frontend
    cliente_nome = serializers.ReadOnlyField(source='cliente.nome')
    mes_formatado = serializers.DateField(source='mes', format="%Y-%m-%d")

    class Meta:
        model = Consumo
        fields = ['id', 'cliente', 'cliente_nome', 'mes_formatado', 'consumo_kwh'] # Adicione 'tipo' se existir no model