from django.db import models
from usuarios.models import Usuario

# Create your models here.

# Esta clase crea una tabla para guardar las categorias:
class Categorias(models.Model):
    nombre = models.CharField(max_length = 255 )
    activo = models.BooleanField(default=True)
    creacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(auto_now=True) 
    class Meta:
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre


class Noticias(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    img = models.ImageField(upload_to='imagenes_noticias/', blank=True, null=True)
    uptdate = models.DateField(auto_now=True)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='autor_noticias')
    categoria = models.ForeignKey(Categorias, on_delete = models.SET_NULL, related_name = 'noticias', null = True)
    paginate_by = 5
    
    class Meta:
        ordering = ['-fecha'] 
    
    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    relacion_post = models.ForeignKey(Noticias, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='comentario_usuario')

    def __str__(self):
        return self.relacion_post.titulo + '' + self.autor.first_name + '' + self.autor.last_name