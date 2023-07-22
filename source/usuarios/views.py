from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Usuario
from .forms import RegistrarUsuarioForm

# Create your views here.

# VISTA BASADA EN CLASES QUE CREA UN USUARIO.

class RegistroView(CreateView):
    model = Usuario
    template_name = 'usuarios/registro.html'
    form_class = RegistrarUsuarioForm


