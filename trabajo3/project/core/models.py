from django.db import models
from django import forms

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.nombre} - $ {self.precio} -  {self.descripcion}"
    
