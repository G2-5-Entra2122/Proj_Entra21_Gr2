from django import forms
from .models import Vaga


class VagasForm(forms.ModelForm):

    class Meta:
        model=Vaga
        fields=[
            'nome',
            'empregador',
            'nivel',
            'descricao',
            'tipo_contrato',
            'local',
            'outras_reg',
            'requisitos',
            'habil_obr',
            'salmin',
            'salmax',
            'beneficios',
        ]

