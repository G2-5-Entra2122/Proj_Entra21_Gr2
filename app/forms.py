
# from django import forms

# from .models import Candidato, Habilidades

# class CandidatoForm(forms.ModelForm):
    
#     class Meta:
#         model = Candidato
#         fields = [
#             'nome',
#             'sobrenome',
#             'cpf',
#             'endereco',
#             'data_nasc',
#             'perfil_linkedin',
#             'nivel',
#             'area',       
#         ]

# class HabilidadesForm(forms.ModelForm):
#     # experiencia = [
#     #     ('0-1-anos', '0-1 anos'),
#     #     ('1-2-anos', '1-2 anos'),
#     #     ('2-3-anos', '2-3 anos'),
#     #     ('3-4-anos', '3-4 anos'),
#     #     ('4-5-anos', '4-5 anos'),
#     #     ('5+-anos', '5+ anos')
#     # ]

#     # tempo = forms.ChoiceField(choices=experiencia, widget=forms.RadioSelect(attrs={'class': 'tempo-container'}))
#     class Meta:
#         model = Habilidades
#         fields = [
#             'habilidades',
#             'tempo'
#         ]

#         widgets = {
#             'tempo': forms.RadioSelect(attrs={
#             'class': 'tempo-container',
#         })
#         }
