from django.urls import path
from django.contrib.auth.views import LoginView
from .views import RegistroView

app_name = 'usuarios'

urlpatterns = [
    path('login/', LoginView.as_view(template_name = 'usuarios/login.html'), name = 'login'),
    path('registrarse/', RegistroView.as_view(), name = 'registrarse')
    
]