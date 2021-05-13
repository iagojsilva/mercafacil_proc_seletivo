from django.db import models

class ContatoVarejo(models.Model):
    nome = models.CharField(max_length=100, null=False)
    celular = models.CharField(max_length=13, null=False)

    def __str__(self) -> str:
        return self.nome