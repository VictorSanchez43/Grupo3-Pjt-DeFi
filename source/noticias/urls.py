from django.urls import path
from noticias import views

app_name = 'noticias'

urlpatterns = [
    path('noticias/', views.VerNoticias.as_view(), name='noticias'),
    path('publicar-noticia/', views.CrearNoticia.as_view(), name='publicar-noticias'),
    path('editar-noticia/<int:pk>', views.EditarNoticia.as_view(), name='editar-noticia'),
    path('eliminar-noticia/<int:pk>', views.EliminarNoticia.as_view(), name='eliminar-noticia'),
    path('noticia-detalle/<int:pk>', views.NoticiaDetalle.as_view(),name='noticia-detalle' ),
    path('borrar-comentario/<int:pk>', views.BorrarComentarioView.as_view(),name='borrar-comentario')
]

