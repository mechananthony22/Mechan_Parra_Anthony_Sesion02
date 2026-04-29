from django.contrib import admin
from .models import Sucursal


@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre', 'ciudad', 'estado']
    list_filter = ['ciudad', 'estado']
    search_fields = ['codigo', 'nombre', 'direccion']