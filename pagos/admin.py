from django.contrib import admin
from .models import Pago


@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ['id', 'encomienda', 'monto', 'metodo_pago', 'estado']
    list_filter = ['estado', 'metodo_pago']