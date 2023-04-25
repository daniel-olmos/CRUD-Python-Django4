from django.db import models
from django.utils import timezone

# Creación de campos de la tabla 'jugos' 
class Jugos(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.CharField(max_length=20)
    stock = models.CharField(max_length=100)
    img = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'jugos' # Le doy de nombre 'jugos' a nuestra tabla en la Base de Datos 
