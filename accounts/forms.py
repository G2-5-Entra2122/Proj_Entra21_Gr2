from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from .models import PerfilCandidato


class CandidatoForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class EmpresaForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# class PerfilCandidatoForm(forms.ModelForm):
#     required_css_class = 'required'

#     data_nasc = forms.DateField(
#         label='Data de Nacimento',
#         widget=forms.DateInput(
#             format='%Y-%m-%d',
#             attrs={
#                 'type': 'date',
#             }),
#         )

#     class Meta:
#         model = PerfilCandidato
#         fields = [
#             'nome', 
#             'sobrenome',
#             'cpf',
#             'cep',
#             'data_nasc',
#             'github',
#             'linkedin',
#             'facebook',
#             'instagram',
#             'descricao',
#         ]

    
#     def __init__(self, *args, **kwargs):
#         super(PerfilCandidato, self).__init__(*args, **kwargs)
#         for field_name, field in self.fields.items():
#             field.widget.attrs['class'] = 'form-control'