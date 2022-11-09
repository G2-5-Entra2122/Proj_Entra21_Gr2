from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from .models import  PerfilEmpresas

class PerfilEmpresasForm(forms.ModelForm):
    class Meta:
        model = PerfilEmpresas
        fields = ['fantasia', 'razao_social', 'cnpj', 'ie', 'endereco', 'tamanho', 'ramo', 'cep', 'telefone', 'apresentacao']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for key, field in self.fields.items():
            field.widget.attrs['Class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label or self.labels[key]

class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for key, field in self.fields.items():
            field.widget.attrs['Class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label or self.labels[key]

class CandidatoForm(UserCreationForm):
    email = forms.EmailField(max_length=100)
    labels = {'email':'Email'}

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for key, field in self.fields.items():
            field.widget.attrs['Class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label or self.labels[key]


    def clean_email(self):
        e = self.cleaned_data['email']
        if User.objects.filter(email=e).exists():
            raise ValidationError(f'O email {e} já está em uso.')
        return e

    
class EmpresaForm(UserCreationForm):
    email = forms.EmailField(max_length=100)
    labels = {'email':'Email'}

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for key, field in self.fields.items():
            field.widget.attrs['Class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label or self.labels[key]

    def clean_email(self):
        e = self.cleaned_data['email']
        if User.objects.filter(email=e).exists():
            raise ValidationError(f'O email {e} já está em uso.')
        return e

