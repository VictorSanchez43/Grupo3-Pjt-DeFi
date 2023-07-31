from typing import Any, Dict
from django.shortcuts import render
from .models import Noticias, Categorias
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import CrearNoticiasForm
from django.urls import reverse

# Create your views here.

class VerNoticias(ListView):
    model = Noticias
    template_name = 'noticias/noticias.html'
    context_object_name = 'noticias'
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categorias.objects.all
        categoria_seleccionada = self.request.GET.get('categoria')
        categoria_id = self.request.GET.get('categoria')
        if categoria_id:
            try:
                categoria_seleccionada = Categorias.objects.get(pk=categoria_id)
                context['categoria'] = categoria_seleccionada.nombre
            except Categorias.DoesNotExist:
                pass
        return context
        
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        #Filtrando por categoria:
        categoria_seleccionada = self.request.GET.get('categoria')
        if categoria_seleccionada:
            queryset = queryset.filter(categoria = categoria_seleccionada)
        return queryset


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
    
    