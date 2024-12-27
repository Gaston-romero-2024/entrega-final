from django.db import models

# Create your models here.

class Seleccion(models.Model):
    pais=models.CharField(max_length=40)
    fecha=models.DateField()
    titular=models.BooleanField()
    imagen=models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{Seleccion.pais} - {Seleccion.fecha} - {Seleccion.titular} - {Seleccion.imagen}"

 
