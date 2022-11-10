from django.contrib import admin

from .models import  PerfilEmpresas

@admin.register(PerfilEmpresas)
class PerfilEmpresasAdmin(admin.ModelAdmin):
    list_display = ('fantasia', 'razao_social', 'tamanho', 'ramo')