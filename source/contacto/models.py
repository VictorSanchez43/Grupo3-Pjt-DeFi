from django.db import models

# Create your models here.

class Contacto(models.Model):
    fecha = models.DateField(auto_now_add=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=50)
    asunto = models.CharField(max_length=100)
    texto = models.TextField()