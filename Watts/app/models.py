from django.db import models

class Locacao(models.Model):
    estado = models.CharField(max_length=50) 
    nome = models.CharField(max_length=100)


