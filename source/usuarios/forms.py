from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegistrarUsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2', 'email', 'telefono', 'fecha_nacimiento', 'domicilio']