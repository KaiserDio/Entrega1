from django.urls import path
from .views import ArticuloCreacion, ArticuloDetalle, ArticuloLista, ClienteCreacion, ClienteLista, VendedorCreacion, VendedorLista, busquedaArticulo, inicio

urlpatterns = [
    path('', inicio, name="index"), #Default view
    path('articulo/lista', ArticuloLista.as_view(), name='ArticuloLista'), #Lista de Articulos
    path('articulo/detalle/<pk>', ArticuloDetalle.as_view(), name='ArticuloDetalle'), #Detalle de un Articulo Particular
    path('articulo/creacion', ArticuloCreacion.as_view(), name='ArticuloCreacion'), #Creacion de un Articulo
    path('cliente/lista', ClienteLista.as_view(), name='ClienteLista'), #Lista de Clientes
    path('cliente/creacion', ClienteCreacion.as_view(), name='ClienteCreacion'), #Creacion de un Cliente
    path('vendedor/lista', VendedorLista.as_view(), name='VendedorLista'), #Lista de Vendedores
    path('vendedor/creacion', VendedorCreacion.as_view(), name='VendedorCreacion'), #Creacion de un Vendedor
    path('articulo/buscar', busquedaArticulo, name="BuscarArticulos"), #Busqueda de Articulos
]