from django.contrib import admin
from gestionPedidos import models

# Register your models here.

admin.site.register(models.Clientes)
admin.site.register(models.Articulos)
admin.site.register(models.Pedidos)