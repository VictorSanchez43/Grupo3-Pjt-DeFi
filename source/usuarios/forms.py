from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class RegistrarUsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = fields = ['first_name', 'last_name','fecha_nacimiento', 'username', 'password1', 'password2', 'email', 'telefono', 'domicilio'] 
        
        widgets = {
            
            'fecha_nacimiento': DateInput(attrs={'class': 'form-control'}),
        
        }