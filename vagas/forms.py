from django import forms
from .models import Vaga


class VagasForm(forms.ModelForm):

    class Meta:
        model=Vaga
        fields=[
            'nome',
            'categoria',
            'nivel',
            'descricao',
            'modalidade',
            'contrato',
            'local',
            'outras_reg',
            'requisitos',
            'habil_obr',
            'salmin',
            'salmax',
            'beneficios',
        ]

