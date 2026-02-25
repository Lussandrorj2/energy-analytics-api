from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    documento = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nome


class Consumo(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name="consumos"
    )
    mes = models.DateField()
    consumo_kwh = models.DecimalField(max_digits=10, decimal_places=2)
    data_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('cliente', 'mes')

    def __str__(self):
        return f"{self.cliente.nome} - {self.mes}"
    