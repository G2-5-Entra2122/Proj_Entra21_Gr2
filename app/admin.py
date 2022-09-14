from django.contrib import admin

from .models import EmpresaRamo, EmpresaTamanho, Empresas

@admin.register(EmpresaRamo)
class EmpresaRamoAdmin(admin.ModelAdmin):
    list_display = ('ramo',)


@admin.register(EmpresaTamanho)
class EmpresaTamanhoAdmin(admin.ModelAdmin):
    list_display = ('tamanho',)


@admin.register(Empresas)
class EmpresasAdmin(admin.ModelAdmin):
    list_display = ('razao_social', 'cnpj', 'ramo')
