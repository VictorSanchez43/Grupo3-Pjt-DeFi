from django import forms
from .models import Noticias

# Clase que crea un formulario para las publicaciones: 

class CrearNoticiasForm(forms.ModelForm):
    class Meta:
        model = Noticias
        fields = ['titulo', 'texto']
        
