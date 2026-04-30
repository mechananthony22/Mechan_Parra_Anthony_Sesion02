from django.contrib import admin
from .models import Articulo, GrupoArticulo, LineaArticulo, ListaPrecio


@admin.register(GrupoArticulo)
class GrupoArticuloAdmin(admin.ModelAdmin):
    list_display = ('nombre_grupo', 'estado')


@admin.register(LineaArticulo)
class LineaArticuloAdmin(admin.ModelAdmin):
    list_display = ('nombre_linea', 'grupo', 'estado')


@admin.register(ListaPrecio)
class ListaPrecioAdmin(admin.ModelAdmin):
    list_display = ('articulo', 'precio_1', 'precio_compra', 'precio_costo')


@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('codigo_articulo', 'descripcion', 'grupo', 'linea', 'stock')
    list_filter = ('grupo', 'linea')
    search_fields = ('codigo_articulo', 'descripcion')
