from django.db import models



class Empresas(models.Model):
    fantasia = models.CharField('Nome Fantasia', max_length=100)
    razao_social = models.CharField('Razão Social', max_length=100)
    cnpj = models.CharField('CNPJ', max_length=14)
    ie = models.CharField('Inscrição Estadual', max_length=6)
    endereco = models.CharField('Endereço', max_length=100)
    
    TAMANHO_CHOICES = (
        ('pequena', 'Pequena'),
        ('media', 'Média'),
        ('grande', 'Grande'),
    )

    tamanho = models.CharField('Tamanho', max_length=7, choices= TAMANHO_CHOICES) 
    
    RAMO_CHOICES = (
        ('tecnologia', 'Tecnologia'),
        ('servicos', 'Serviços'),
        ('financeiro', 'Financeiro'),
        ('varejo', 'Varejo'),
        ('atacado', 'Atacado'),
        ('industria', 'Industria'),
        ('comercio', 'Comércio')
    )
    ramo = models.CharField('Ramo', max_length=50, choices=RAMO_CHOICES)
    cep = models.CharField('CEP', max_length=8,)
    email = models.EmailField('Email', max_length=100)
    telefone = models.IntegerField('Telefone', max_length=11)
    apresentacao = models.CharField('Apresentação', max_length=500)
    #logo = models.ImageField('Logo') limitar o tamanho da logo


    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'


    def _str_(self):
        return self.fantasia
        

