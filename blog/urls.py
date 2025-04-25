from django.urls import path
from .views import (
    ArticuloListView, ArticuloDetailView, ArticuloCreateView,
    ArticuloUpdateView, ArticuloDeleteView,
    AutorListView, AutorCreateView,
    CategoriaListView, CategoriaCreateView,
)

urlpatterns = [
    # Articulos
    path('articulos/', ArticuloListView.as_view(), name='articulo_list'),
    path('articulos/<int:pk>/', ArticuloDetailView.as_view(), name='articulo_detail'),
    path('articulos/nuevo/', ArticuloCreateView.as_view(), name='articulo_create'),
    path('articulos/<int:pk>/editar/', ArticuloUpdateView.as_view(), name='articulo_update'),
    path('articulos/<int:pk>/eliminar/', ArticuloDeleteView.as_view(), name='articulo_delete'),

  
    path('autores/', AutorListView.as_view(), name='autor_list'),
    path('autores/nuevo/', AutorCreateView.as_view(), name='autor_create'),

    
    path('categorias/', CategoriaListView.as_view(), name='categoria_list'),
    path('categorias/nuevo/', CategoriaCreateView.as_view(), name='categoria_create'),
]
