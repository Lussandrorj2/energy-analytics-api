from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    documento = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nome