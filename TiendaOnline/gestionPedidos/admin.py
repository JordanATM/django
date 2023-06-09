from django.contrib import admin
from gestionPedidos import models

# Register your models here.

class Clientes_admin(admin.ModelAdmin):
    list_display=("nombre","direccion","email","telefono")
    search_fields=("nombre","email","telefono",)

class Articulos_admin(admin.ModelAdmin):
    list_display=("nombre","seccion","precio")
    search_fields=("nombre","seccion","precio",)
    list_filter=("seccion",)

class Pedido_admin(admin.ModelAdmin):
    list_display=("numero","fecha","entregado")
    search_fields=("numero","fecha","entregado",)
    list_filter=("fecha",)
    date_hierarchy="fecha"

admin.site.register(models.Clientes, Clientes_admin)
admin.site.register(models.Articulos,Articulos_admin)
admin.site.register(models.Pedidos,Pedido_admin)