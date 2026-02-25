from django.contrib import admin
from .models import Cliente, Consumo


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'documento')

@admin.register(Consumo)
class ConsumoAdmin(admin.ModelAdmin):
    list_display = ('id','cliente','mes','consumo_kwh')