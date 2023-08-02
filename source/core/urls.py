from django.urls import path, include
from core import views

urlpatterns = [
    path('', views.indexView, name='index'),
    path('index/', views.indexView, name='index'),
    path('usuarios/', include('usuarios.urls')),
    path('noticias/', include('noticias.urls')),
    path('contacto/', include('contacto.urls')),
    path('finanzas/', include('finanzas.urls')),
    path('acerca_de/', include('acerca_de.urls')),
]