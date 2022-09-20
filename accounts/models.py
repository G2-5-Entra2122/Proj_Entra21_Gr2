from django.db import models
from django.contrib.auth.models import User

class PerfilCandidato(models.Model):
    nome = models.CharField('Nome', max_length=50, null=True)
    sobrenome = models.CharField('Sobrenome', max_length=50, null=True)
    cpf = models.CharField('CPF', max_length=14, null=True)
    cep = models.CharField('CEP', max_length=9, null=True)
    data_nasc = models.DateField('Data de Nascimento', max_length=10 , null=True)
    github = models.CharField('GitHub', max_length=100, default='#')
    linkedin = models.CharField('Linkedin', max_length=100, default='#')
    facebook = models.CharField('Facebook', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')
    descricao = models.TextField('Descrição', max_length=200, null=True)
    usuario = models.OneToOneField(User, on_delete=models.PROTECT)
