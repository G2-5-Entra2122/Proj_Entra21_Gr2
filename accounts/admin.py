from django.contrib import admin

from .models import PerfilCandidatos, PerfilEmpresas

@admin.register(PerfilCandidatos)
class PerfilCandidatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'data_nasc')

@admin.register(PerfilEmpresas)
class PerfilEmpresasAdmin(admin.ModelAdmin):
    list_display = ('fantasia', 'razao_social', 'tamanho', 'ramo')