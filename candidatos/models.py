from django.db import models
from django.contrib.auth.models import User

class Habilidades(models.Model):

    habilidade = models.CharField('Habilidade', max_length=15,  null=True, blank=True)
    
    class Meta:
        verbose_name = 'Habilidade'
        verbose_name_plural = 'Habilidades'

    
    def __str__(self):
        return f'{self.habilidade}'



class Curriculo(models.Model):
    CATEGORIA_CHOICES = (
        ('Full-stack', 'Full-Stack'),
        ('Front-end', 'Front-end'),
        ('Back-end', 'Back-end'),
        ('Mobile', 'Mobile'),
    )
    categoria = models.CharField('Área', max_length=10, choices=CATEGORIA_CHOICES, null=True)    
    
    
    NIVEL_CHOICES = (
        ('Junior','Junior'),
        ('Pleno','Pleno'),
        ('Sênior','Sênior')
        )
    nivel = models.CharField('Nível', max_length=6, choices=NIVEL_CHOICES, null=True)
    
    
    CONTRATO_CHOICES = (
        ('Estágio', 'Estágio'),
        ('CLT', 'CLT'),
        ('Freelance', 'Freelance'),
        ('PJ', 'PJ'),
        ('Voluntário', 'Voluntário'),
    )
    contrato = models.CharField('Contrato', max_length=7, choices=CONTRATO_CHOICES, null=True)

    
    MODALIDADE_CHOICES = (
        ('Presencial','Presencial'),
        ('Híbrido','Híbrido'),
        ('Remoto','Remoto')
    )
    modalidade = models.CharField('Local', max_length=10, choices=MODALIDADE_CHOICES, null=True)

    
    salario = models.IntegerField(verbose_name='Salário desejado', null=True)
    
    
    habilidade_pri = models.ForeignKey(Habilidades, verbose_name='1ª - Habilidade')
    habilidade_seg = models.ForeignKey(Habilidades, verbose_name='2ª - Habilidade')
    habilidade_ter = models.ForeignKey(Habilidades, verbose_name='3ª - Habilidade')
    habilidade_qua = models.ForeignKey(Habilidades, verbose_name='4ª - Habilidade')
    habilidade_qui = models.ForeignKey(Habilidades, verbose_name='5ª - Habilidade')

    
    usuario = models.OneToOneField(User, on_delete=models.PROTECT)

    
    class Meta:
        verbose_name = 'Curriculo'
        verbose_name_plural = 'Curriculos'

    
    def __str__(self):
        return f'{self.categoria} - {self.nivel} - {self.modalidade}'

