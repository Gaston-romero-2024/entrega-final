from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Mensaje(models.Model):
    nombre=models.CharField(max_length=40)
    email=models.EmailField()
    asunto=models.CharField(max_length=100)
    mensajes=models.TextField()
    fecha=models.DateField(auto_now_add=True)

