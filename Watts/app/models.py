from django.db import models

class Locacao(models.Model):
    estado = models.CharField(max_length=50) 
    nome = models.CharField(max_length=100)



class Comodo(models.Model):
    locacao = models.ForeignKey(Locacao, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)