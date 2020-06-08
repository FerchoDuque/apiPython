from django.db import models

# Create your models here.
class Producto(models.Model):
     PRODUCT_STATE = (
         ('E','Entrada'),
         ('S','Salida'),
         ('D','Defectuoso'),
     )
     codigo = models.CharField(max_length=35, unique=True )
     nombre = models.CharField(max_length=85)
     estado = models.CharField(max_length=1, choices=PRODUCT_STATE)
     fecha_ingreso = models.DateTimeField(auto_now=True)
