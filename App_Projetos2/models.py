from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

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
        return f"Nome: {self.nome_doador} / Número: {self.telefone_doador} / Tipo: {self.tipo_doacao}"

class Inscricao(models.Model):
    nome = models.CharField(max_length=256)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    mensagem = models.TextField()

    def __str__(self):
        return self.nome
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    pontos = models.IntegerField(default=0)

    def __str__(self):
        return f"Nome: {self.user.username} / Pontos: {self.pontos}"
