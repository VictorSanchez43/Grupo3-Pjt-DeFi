from django.shortcuts import render
from .models import Finanzas
from django.views.generic import ListView

# Create your views here.

class VerFinanzas(ListView):
    model = Finanzas
    template_name = 'finanzas/finanzas.html'
    context_object_name = 'finanzas'
