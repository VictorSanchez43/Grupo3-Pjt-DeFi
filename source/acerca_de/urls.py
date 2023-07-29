from django.urls import path
from .views import acercaDeView

app_name = 'acerca_de'

urlpatterns = [
    path('acerca_de/', acercaDeView, name='acerca_de'),
]