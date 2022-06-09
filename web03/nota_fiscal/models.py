from django.db import models

class NotaFiscal(models.Model):

    produto = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    data = models.CharField(max_length=100)
    valor = models.CharField(max_length=100)

def __str__(self):
    return self.nome