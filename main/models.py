from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nome = models.CharField(max_length=30)
    
    def __str__(self):
        return str(self.nome)


class Receita(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)
    descricao = models.CharField(max_length=100)
    valor = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    data = models.DateField(auto_now_add=True)


class Despesa(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)
    descricao = models.CharField(max_length=100)
    valor = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    data = models.DateField(auto_now_add=True, null=True, blank=True)

