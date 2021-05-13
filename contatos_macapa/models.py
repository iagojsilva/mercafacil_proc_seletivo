from django.db import models

class ContatoMacapa(models.Model):
    nome = models.CharField(max_length=200, null=False)
    celular = models.CharField(max_length=20, null=False)

    def __str__(self) -> str:
        return self.nome