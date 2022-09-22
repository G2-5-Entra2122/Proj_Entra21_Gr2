from django import forms
from models import Vaga

# form
class VagasForm(forms.ModelForm):

    class Meta:
        model=Vaga
        fields=[
            'nome',
            'nivel',
            'descricao',
            'tipo_contrato',
            'local',
            'outras_reg',
            'requisitos',
            'habil_obr',
            'salmin',
            'salmax',
            'beneficios'
        ]

