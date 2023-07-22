from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
def get_lista_fechas_nacimiento():
# Generar una lista de opciones de fechas de nacimiento (año-mes)
    lista_fechas = []
    for year in range(1900, 2023):
        for month in range(1, 13):
            fecha = f"{year}-{str(month).zfill(2)}"
            lista_fechas.append((fecha, fecha))
    return lista_fechas

class Usuario(AbstractUser):
    telefono = models.CharField(max_length=50)
    fecha_nacimiento = models.CharField(max_length=10, choices=get_lista_fechas_nacimiento())
    domicilio = models.CharField(max_length=100, blank=True, null=True)
    es_admin = models.BooleanField(default=False)
    es_colab = models.BooleanField(default=False)
    
    def __str__(self):
        return self.first_name + '-' + self.last_name
    



    
    
