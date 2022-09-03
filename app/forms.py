from django import forms
from .models import Candidato

class CandidatoForm(forms.ModelForm):
    
    class Meta:
        model = Candidato
        fields = [
            'nome',
            'sobrenome',
            'cpf',
            'endereco',
            'data_nasc',
            'perfil_linkedin',
            'nivel',
            'area',
            'habilidades'       
        ]