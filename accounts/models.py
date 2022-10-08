from django.db import models
from django.contrib.auth.models import User

class PerfilCandidatos(models.Model):
    nome = models.CharField('Nome', max_length=50, null=True)
    sobrenome = models.CharField('Sobrenome', max_length=50, null=True)
    cpf = models.CharField('CPF', max_length=14, null=True)
    cep = models.CharField('CEP', max_length=9, null=True)
    data_nasc = models.DateField('Data de Nascimento', max_length=10 , null=True)
    github = models.CharField('GitHub', max_length=100, null=True, blank=True , help_text='URL do seu perfil no GitHub')
    linkedin = models.CharField('Linkedin', max_length=100, null=True, blank=True , help_text='URL do seu perfil no LinkedIn')
    facebook = models.CharField('Facebook', max_length=100, null=True, blank=True , help_text='URL do seu perfil no Facebook')
    instagram = models.CharField('Instagram', max_length=100, null=True, blank=True , help_text='URL do seu perfil no Instagram')
    descricao = models.TextField('Descrição', max_length=300, null=True, blank=True , help_text='Resumo do seu perfil profissional em no máximo 300 caracteres.')
    usuario = models.OneToOneField(User, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Candidato'
        verbose_name_plural = 'Candidatos'


    def _str_(self):
        return self.nome

class PerfilEmpresas(models.Model):
    fantasia = models.CharField('Nome Fantasia', max_length=100, null=True,help_text='Nome fantasia da sua empresa')
    razao_social = models.CharField('Razão Social', max_length=100, null=True,help_text='Razão social da sua empresa')
    cnpj = models.CharField('CNPJ', max_length=18, null=True,help_text='Apenas números')
    ie = models.CharField('Inscrição Estadual', max_length=20, null=True, blank=True,help_text='Inscrição estadual da sua empresa')
    endereco = models.CharField('Endereço', max_length=100, null=True)
    
    TAMANHO_CHOICES = (
        ('pequena', 'Pequena'),
        ('media', 'Média'),
        ('grande', 'Grande'),
    )

    tamanho = models.CharField('Tamanho', max_length=7, choices= TAMANHO_CHOICES, null=True) 
    
    RAMO_CHOICES = (
        ('tecnologia', 'Tecnologia'),
        ('servicos', 'Serviços'),
        ('financeiro', 'Financeiro'),
        ('varejo', 'Varejo'),
        ('atacado', 'Atacado'),
        ('industria', 'Industria'),
        ('comercio', 'Comércio')
    )
    ramo = models.CharField('Ramo', max_length=50, choices=RAMO_CHOICES, null=True)
    cep = models.CharField('CEP', max_length=9, null=True,help_text='Apenas números')
    telefone = models.CharField('Telefone', max_length=15, null=True,help_text='Apenas números, com prefixo DDD em 2 dígitos')
    apresentacao = models.TextField('Apresentação', max_length=500,help_text='Apresente sua empresa em no máximo 500 caracteres')
    usuario = models.OneToOneField(User, on_delete=models.PROTECT)
    #logo = models.ImageField('Logo') limitar o tamanho da logo


    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'


    def _str_(self):
        return self.fantasia
        
