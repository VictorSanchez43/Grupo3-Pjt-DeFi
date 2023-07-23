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
