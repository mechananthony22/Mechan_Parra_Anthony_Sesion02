from django.contrib import admin
from .models import Usuario, Perfil

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('perfil_nombre',)
