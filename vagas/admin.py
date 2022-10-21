from django.contrib import admin
from .models import Vaga

@admin.register(Vaga)
class VagaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nivel', 'categoria','modalidade')