from django.db import models, migrations
from django.contrib.auth.models import User

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
        
