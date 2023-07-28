from django.urls import path
from .views import ContactoView, contacto_ok

app_name = 'contacto'

urlpatterns = [
    path('contacto/', ContactoView.as_view(), name='contacto'),
    path('contacto-exitoso/', contacto_ok, name='contacto-exitoso'),
]