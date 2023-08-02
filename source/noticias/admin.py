from django.contrib import admin
from .models import Noticias, Categorias, Comentario

# Register your models here.

admin.site.register(Noticias)
admin.site.register(Categorias)
admin.site.register(Comentario)

