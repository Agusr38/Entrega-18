from django.db import models

# Create your models here.

class familiares(models.Model):
    nombre_apellido = models.CharField(max_length=30)
    Edad = models.IntegerField()
    profesion = models.CharField(max_length=30)
