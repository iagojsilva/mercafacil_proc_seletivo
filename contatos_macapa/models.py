from django.db import models

class ContatoMacapa(models.Model):
    name = models.CharField(max_length=200, null=False)
    cellphone = models.CharField(max_length=20, null=False)

    def __str__(self) -> str:
        return self.name