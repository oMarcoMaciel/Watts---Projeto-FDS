from django.db import models

class Locacao(models.Model):
    estado = models.CharField(max_length=50) 
    nome = models.CharField(max_length=100)

class PontoDeEnergia(models.Model):
    estado = models.CharField(max_length=50) 
    nome = models.CharField(max_length=100)
    comodo= models.CharField(max_length=100)
    gastos = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)


#class Comodo(models.Model):
    #locacao = models.ForeignKey(Locacao, on_delete=models.CASCADE)
