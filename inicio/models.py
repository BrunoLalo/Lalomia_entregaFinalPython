from django.db import models

class Zapatilla(models.Model):
    marca = models.CharField(max_length=15)
    color = models.CharField(max_length=15)
    talle = models.IntegerField()
    precio = models.IntegerField()
    