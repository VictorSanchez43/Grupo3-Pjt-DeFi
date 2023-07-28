from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class RegistrarUsuarioForm(UserCreationForm):
    fecha_nacimiento = forms.DateField(widget=DateInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'fecha_nacimiento', 'username', 'password1', 'password2', 'email', 'telefono', 'domicilio']
        
    
        labels = {
            'first_name': 'Ingresa tu nombre',
            'last_name': 'Ingresa tu Apellido',
            'username': 'Ingresa un Nombre de Usuario',
            'emai': 'correo electronico',
            'telefono': 'telefono',
            'domicilio':'domicilio'
            }
        
