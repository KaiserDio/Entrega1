from django.db import models

# Create your models here.

class Articulo(models.Model):
    nombre=models.CharField(max_lenght=40)
    descripcion=models.CharField(max_lenght=40)
    precio=models.IntegerField()
    cantidad=models.IntegerField()
    

class Cliente(models.Model):
    nombre=models.CharField(max_lenght=40)
    apellido=models.IntegerField()
    telefono=models.IntegerField()
    direccion=models.CharField(max_lenght=40)

class Venta(models.Model):
    idCliente=models.IntegerField()
    idArticulo=models.IntegerField()
    cantidad=models.IntegerField()
    precioTotal=models.IntegerField()


class Vendedor(models.Model):
    nombre=models.CharField(max_lenght=40)
    apellido=models.IntegerField()
    sueldo=models.IntegerField()
    