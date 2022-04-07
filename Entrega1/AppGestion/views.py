from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import buscar_articulos_forms

from .models import Articulo, Cliente, Vendedor

# Create your views here.
def inicio(request):
    
    return render(request, "AppGestion/index.html" )

#Views ARTICULOS
class ArticuloLista(ListView):
    model = Articulo
    template_name = "AppGestion/articulo_lista.html"

class ArticuloDetalle(DetailView):
    model = Articulo
    template_name = "AppGestion/articulo_detalle.html"

class ArticuloCreacion(CreateView):
    model = Articulo
    success_url = '/articulo/lista'
    template_name = 'AppGestion/articulo_creacion.html'
    fields = ['nombre', 'descripcion', 'precio', 'cantidad']

def busquedaArticulo(request):
    search_form = buscar_articulos_forms()

    nombre= request.GET.get('nombre')

    if nombre:
        print(nombre)

        form_with_data = buscar_articulos_forms(request.GET)

        if form_with_data.is_valid():

            articulos = Articulo.objects.filter(nombre__icontains=nombre).all()
            print(articulos)

            if(articulos):
                return render(request, "AppGestion/articulo_buscar.html", {"search_form": search_form, "resultados": articulos})
            else:
                return render(request, "AppGestion/articulo_buscar.html", {"search_form": search_form, "resultados": None, "buscado": True})

        return render(request, "AppGestion/articulo_buscar.html", {"search_form": search_form, "resultados": None, "resultados": None,  "error": form_with_data.errors})

    return render(request, "AppGestion/articulo_buscar.html", {"search_form": search_form, "resultados": None, "error": None})


#Views CLIENTES
class ClienteLista(ListView):
    model = Cliente
    template_name = "AppGestion/cliente_lista.html"
    

class ClienteCreacion(CreateView):
    model = Cliente
    success_url = '/cliente/lista'
    template_name = 'AppGestion/cliente_creacion.html'
    fields = ['nombre', 'apellido', 'telefono', 'direccion']

#Views VENDEDOR
class VendedorLista(ListView):
    model = Vendedor
    template_name = "AppGestion/vendedor_lista.html"

class VendedorCreacion(CreateView):
    model = Vendedor
    success_url = "/vendedor/lista"
    template_name = 'AppGestion/vendedor_creacion.html'
    fields = ['nombre', 'apellido', 'sueldo']