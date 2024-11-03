from django.db import models

class Zapatilla(models.Model):
    marca = models.CharField(max_length=15)
    color = models.CharField(max_length=15)
    talle = models.IntegerField()
    precio = models.IntegerField()
    fecha = models.DateField(blank=True, null=True)
    imagen = models.ImageField(upload_to='zapatillas', blank=True, null=True)
    
    def __str__(self):
        return  f'{self.id}'