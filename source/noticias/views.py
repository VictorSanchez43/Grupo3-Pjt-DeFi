from django.shortcuts import render
from .models import Noticias
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import CrearNoticiasForm
from django.urls import reverse

# Create your views here.

class VerNoticias(ListView):
    model = Noticias
    template_name = 'noticias/noticias.html'
    context_object_name = 'noticias'
    
    def get_queryset(self):
        consulta_anterior = super().get_queryset()
        consulta_ordenada = consulta_anterior.order_by('fecha')
        return consulta_ordenada


# Vista que renderiza las noticias:

class CrearNoticia(CreateView):
    model = Noticias
    template_name = 'noticias/publicar-noticias.html'
    form_class = CrearNoticiasForm
    
    def get_success_url(self):
        return reverse('noticias:noticias')
    
    def form_valid(self, form):
        f = form.save(commit=False) 
        f.autor_id = self.request.user.id
        return super().form_valid(f)
    

# Vista que edita las noticias

class EditarNoticia(UpdateView):
    model = Noticias
    template_name = 'noticias/editar-noticia.html'
    form_class = CrearNoticiasForm
    
    def get_success_url(self):
        return reverse('noticias:noticias')

# Vista que elimina una noticia:

class EliminarNoticia(DeleteView):
    model = Noticias
    template_name = 'noticias/eliminar-noticias.html'
    
    def get_success_url(self):
        return reverse('noticias:noticias')
    

#Vista que crea un noticia en detalle:

class NoticiaDetalle(DetailView):
    model = Noticias
    template_name = 'noticias/noticia-detalle.html'
    context_object_name = 'detalle'
