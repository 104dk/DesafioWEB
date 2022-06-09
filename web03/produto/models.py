from django.db import models

class Produto(models.Model):

    marca = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    validade = models.CharField(max_length=100)
    data = models.CharField(max_length=100)
    valor = models.CharField(max_length=100)


def __str__(self):
    return self.nome