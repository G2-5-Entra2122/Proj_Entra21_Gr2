from django.contrib import admin

from .models import EmpresaRamo, EmpresaTamanho, Empresas, Candidato, Habilidades, Nivel, Area

@admin.register(EmpresaRamo)
class EmpresaRamoAdmin(admin.ModelAdmin):
    list_display = ('ramo',)


@admin.register(EmpresaTamanho)
class EmpresaTamanhoAdmin(admin.ModelAdmin):
    list_display = ('tamanho',)


@admin.register(Empresas)
class EmpresasAdmin(admin.ModelAdmin):
    list_display = ('razao_social', 'cnpj', 'ramo')


@admin.register(Nivel)
class NivelAdmin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(Habilidades)
class HabilidadesAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tempo')


@admin.register(Candidato)
class CandidatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nivel', 'area')
