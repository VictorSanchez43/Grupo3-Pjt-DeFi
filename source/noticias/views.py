from django.shortcuts import render
from .models import Noticias
from django.views.generic import ListView

# Create your views here.

class VerNoticias(ListView):
    model = Noticias
    template_name = 'noticias/noticias.html'
    context_object_name = 'noticias'
    
    def get_queryset(self):
        consulta_anterior = super().get_queryset()
        consulta_ordenada = consulta_anterior.order_by('fecha')
        return consulta_ordenada

