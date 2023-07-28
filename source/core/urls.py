from django.urls import path, include
from core import views

urlpatterns = [
    path('index/', views.indexView, name='index'),
    path('usuarios/', include('usuarios.urls')),
    path('noticias/', include('noticias.urls')),
    path('contacto/', include('contacto.urls'))
]