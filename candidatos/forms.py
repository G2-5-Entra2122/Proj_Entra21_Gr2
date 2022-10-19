from django import forms

from .models import Curriculo

class CurriculoForm(forms.ModelForm):

    class Meta:
        model = Curriculo
        fields = [
        'categoria',
        'nivel', 
        'contrato', 
        'modalidade',
        'salario',
        'pri_habilidade_candidato',
        'seg_habilidade_candidato',
        'ter_habilidade_candidato',
        'qua_habilidade_candidato',
        'qui_habilidade_candidato'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for key, field in self.fields.items():
            field.widget.attrs['Class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label or self.labels[key]