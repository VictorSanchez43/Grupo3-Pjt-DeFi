from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    telefono = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(auto_now=False, verbose_name='Fecha Nacimiento', null=True, blank=True)
    domicilio = models.CharField(max_length=100, blank=True, null=True)
    es_admin = models.BooleanField(default=False)
    es_colab = models.BooleanField(default=False)
    
    def __str__(self):
        return self.first_name + '-' + self.last_name
    



    
    
