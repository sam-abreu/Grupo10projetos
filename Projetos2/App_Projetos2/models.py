from django.db import models

# Create your models here.
class Brinquedo(models.Model):
    nome = models.CharField(max_length=256)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    faixaetaria = models.CharField(max_length=256)
    material = models.CharField(max_length=256)

    def __str__(self):
        return self.nome
    

class Doacao(models.Model):
    nome_doador = models.CharField(max_length=100)
    email_doador = models.EmailField()
    telefone_doador = models.CharField(max_length=15, blank=True)
    tipo_doacao = models.CharField(max_length=100)  # Agora o tipo de doação é livre
    descricao = models.TextField(help_text='Descreva o estado do brinquedo ou material têxtil')
    data_doacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome_doador} - {self.tipo_doacao}"
