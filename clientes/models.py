from django.db import models

# Create your models here.
class Empresa(models.Model):
    razon_social=models.TextField(max_length=50)
    direccion=models.TextField()
    cuit=models.TextField(max_length=11)
    email=models.EmailField()
    telefono=models.CharField(max_length=14)
    fecha_registro=models.DateField()
    


