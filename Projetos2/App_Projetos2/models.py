from django.db import models

# Create your models here.
class Brinquedo(models.Model):
    nome = models.CharField(max_length=256)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    faixaetaria = models.CharField(max_length=256)
    material = models.CharField(max_length=256)

    def __str__(self):
        return self.nome