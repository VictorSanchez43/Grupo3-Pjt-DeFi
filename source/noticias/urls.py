from django.urls import path
from noticias import views

app_name = 'noticias'

urlpatterns = [
    path('noticias/', views.VerNoticias.as_view(), name='noticias'),
    path('publicar-noticia/', views.CrearNoticia.as_view(), name='publicar-noticias'),
    path('editar-noticia/<int:pk>', views.EditarNoticia.as_view(), name='editar-noticia'),
]

