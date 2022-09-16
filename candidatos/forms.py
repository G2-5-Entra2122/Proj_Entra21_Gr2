from django import forms
from .models import Habilidades, Candidatos


class CandidatosForm(forms.ModelForm):
    required_css_class = 'required'

    data_nasc = forms.DateField(
        label='Data de Nacimento',
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'type': 'date',
            }),
        )

    class Meta:
        model = Candidatos
        fields = [
            'nome', 
            'sobrenome',
            'cpf',
            'cep',
            'data_nasc',
            'github',
            'linkedin',
            'facebook',
            'instagram',
            'descricao',
        ]
    
    def __init__(self, *args, **kwargs):
        super(CandidatosForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'



class HabilidadesForm(forms.ModelForm):
    
    class Meta:
        model = Habilidades
        fields = [
            'habilidade',
            'experiencia'
        ]

        widgets = {
            'experiencia': forms.RadioSelect(attrs={
            'class': 'tempo-container',
        })
        }


