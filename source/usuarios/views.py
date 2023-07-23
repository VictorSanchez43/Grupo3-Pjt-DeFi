from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Usuario
from .forms import RegistrarUsuarioForm
from django.urls import reverse

# Create your views here.

# VISTA BASADA EN CLASES QUE CREA UN USUARIO.

class RegistroView(CreateView):
    model = Usuario
    template_name = 'usuarios/registro.html'
    form_class = RegistrarUsuarioForm
    
    def get_success_url(self):
        return reverse('index')


