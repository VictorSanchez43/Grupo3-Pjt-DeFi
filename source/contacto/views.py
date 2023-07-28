from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Contacto
from .forms import ContactoForm
from django.urls import reverse
# Create your views here.

class ContactoView(CreateView):
    model = Contacto
    template_name = 'contacto/contacto.html'
    form_class = ContactoForm

    def get_success_url(self):
        return reverse('contacto:contacto-exitoso')

def contacto_ok(request):
    return render(request, 'contacto/contacto-exitoso.html', {})