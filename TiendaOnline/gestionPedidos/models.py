from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50, verbose_name="Dirección")
    email = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=15, verbose_name="Teléfono")

    # def __str__(self):
    #     return "Nombre del cliente: %s"%(self.nombre)

class Articulos(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=30, verbose_name="Sección")
    precio = models.IntegerField()

    def __str__(self):
        return "Articulo: %s | sección: %s | precio: %s"%(self.nombre, self.seccion, self.precio)

class Pedidos(models.Model):
    numero = models.IntegerField(verbose_name="Número")
    fecha = models.DateField()
    entregado = models.BooleanField()