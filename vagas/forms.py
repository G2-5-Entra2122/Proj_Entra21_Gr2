from django.forms import Form, CharField, ChoiceField
from django import forms
from .models import Vaga


class VagaForm(forms.ModelForm):

    class Meta:
        model = Vaga
        fields=[
            'nome',
            'categoria',
            'nivel',
            'descricao',
            'modalidade',
            'contrato',
            'jornada',
            'local',
            'outras_reg',
            'requisitos',
            'salmin',
            'salmax',
            'beneficios',
            'pri_habilidade_vaga',
            'seg_habilidade_vaga',
            'ter_habilidade_vaga',
            'qua_habilidade_vaga',
            'qui_habilidade_vaga',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for key, field in self.fields.items():
            field.widget.attrs['Class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label or self.labels[key]

class FilterForm(Form):
    CATEGORIA_CHOICES = (
        ('Full-stack', 'Full-Stack'),
        ('Front-end', 'Front-end'),
        ('Back-end', 'Back-end'),
        ('Mobile', 'Mobile')
    )
    search = CharField(required=False)
    filter_field = ChoiceField(choices=CATEGORIA_CHOICES)

    NIVEIS_CHOICES=[
        ('Junior','Junior'),
        ('Pleno','Pleno'),
        ('Sênior','Sênior')
    ]
    search = CharField(required=False)
    filter_field = ChoiceField(choices=NIVEIS_CHOICES)

    MODALIDADES_CHOICES=[
        ('Presencial','Presencial'),
        ('Híbrido','Híbrido'),
        ('Remoto','Remoto')
    ]
    search = CharField(required=False)
    filter_field = ChoiceField(choices=MODALIDADES_CHOICES)

    CONTRATO_CHOICES = [
        ('Estágio', 'Estágio'),
        ('CLT', 'CLT'),
        ('Freelance', 'Freelance'),
        ('PJ', 'PJ'),
        ('Voluntário', 'Voluntário'),
    ]
    search = CharField(required=False)
    filter_field = ChoiceField(choices=CONTRATO_CHOICES)

    JORNADA_CHOICES = [
        ('Período Integral', 'Período Integral'),
        ('Meio Preíodo', 'Meio Período'),
    ]
    search = CharField(required=False)
    filter_field = ChoiceField(choices=JORNADA_CHOICES)

    OUTRAS_REG_CHOICES=[
        ('sim','Sim'),
        ('nao','Não')
    ]
    search = CharField(required=False)
    filter_field = ChoiceField(choices=OUTRAS_REG_CHOICES)
