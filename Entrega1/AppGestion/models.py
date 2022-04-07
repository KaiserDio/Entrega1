from django.db import models

# Create your models here.

class Articulo(models.Model):

    nombre=models.CharField(max_length=40)
    descripcion=models.CharField(max_length=40)
    precio=models.IntegerField()
    cantidad=models.IntegerField()

    def __str__(self):
        return (f"nombre: {self.nombre}, descripcion: {self.descripcion}, descripcion: {self.precio}, descripcion: {self.cantidad}")
    
class Cliente(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    telefono=models.IntegerField()
    direccion=models.CharField(max_length=40)

    def __str__(self):
        return (f"nombre: {self.nombre}, descripcion: {self.apellido}, descripcion: {self.telefono}, descripcion: {self.direccion}")


class Vendedor(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    sueldo=models.IntegerField()

    def __str__(self):
        return (f"nombre: {self.nombre}, descripcion: {self.apellido}, descripcion: {self.sueldo}")
    