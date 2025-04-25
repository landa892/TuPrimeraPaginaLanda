from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Articulo, Autor, Categoria


class ArticuloListView(ListView):
    model = Articulo
    template_name = 'articulos/articulo_list.html'

class ArticuloDetailView(DetailView):
    model = Articulo
    template_name = 'articulos/articulo_detail.html'

class ArticuloCreateView(CreateView):
    model = Articulo
    fields = '__all__'
    template_name = 'articulos/articulo_form.html'
    success_url = reverse_lazy('articulo_list')

class ArticuloUpdateView(UpdateView):
    model = Articulo
    fields = '__all__'
    template_name = 'articulos/articulo_form.html'
    success_url = reverse_lazy('articulo_list')

class ArticuloDeleteView(DeleteView):
    model = Articulo
    template_name = 'articulos/articulo_confirm_delete.html'
    success_url = reverse_lazy('articulo_list')


class AutorListView(ListView):
    model = Autor
    template_name = 'autores/autor_list.html'

class AutorCreateView(CreateView):
    model = Autor
    fields = '__all__'
    template_name = 'autores/autor_form.html'
    success_url = reverse_lazy('autor_list')


class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categorias/categoria_list.html'

class CategoriaCreateView(CreateView):
    model = Categoria
    fields = '__all__'
    template_name = 'categorias/categoria_form.html'
    success_url = reverse_lazy('categoria_list')

