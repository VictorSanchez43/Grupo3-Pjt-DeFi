from django.db import models
from usuarios.models import Usuario

# Create your models here.

class Noticias(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    img = models.ImageField(upload_to='imagenes_noticias/', blank=True, null=True)
    uptdate = models.DateField(auto_now=True)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='autor_noticias')
    
    def __str__(self):
        return self.titulo
