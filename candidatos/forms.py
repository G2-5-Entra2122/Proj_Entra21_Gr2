from django import forms
from .models import Habilidades


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
