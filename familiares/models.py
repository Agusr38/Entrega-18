from django.db import models
from datetime import datetime

# Create your models here.

class familiares(models.Model):
    nombre_apellido = models.CharField(max_length=30)
    Edad = models.IntegerField()
    fecha_nacimiento = str(models.DateField())
