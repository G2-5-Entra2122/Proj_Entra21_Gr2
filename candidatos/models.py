from django.db import models
from django.contrib.auth.models import User

class Habilidades(models.Model):
    HABILIDADES_CHOICES = [
        ('Python', 'Python'),
        ('JavaScript', 'JavaScript'),
        ('TypeScript', 'TypeScript'),
        ('Django', 'Django'),
        ('PHP', 'PHP')
    ]
    habilidade = models.CharField('Habilidade', max_length=15, choices=HABILIDADES_CHOICES, null=True)
    
    
    EXPERIENCIA_CHOICES = [
        ('0-1-anos', '0-1 anos'),
        ('1-2-anos', '1-2 anos'),
        ('2-3-anos', '2-3 anos'),
        ('3-4-anos', '3-4 anos'),
        ('4-5-anos', '4-5 anos'),
        ('5+-anos', '5+ anos')
    ]
    experiencia = models.CharField('Tempo de experiência', max_length=15, choices=EXPERIENCIA_CHOICES, blank=False, default='Unspecified', null=True)

    
    class Meta:
        verbose_name = 'Habilidade'
        verbose_name_plural = 'Habilidades'

    
    def __str__(self):
        return f'{self.habilidade}({self.experiencia})'



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

    
    JORNADA_CHOICES = (
        ('Período Integral', 'Período Integral'),
        ('Meio Preíodo', 'Meio Período'),
    )
    jornada = models.CharField('Jornada', max_length=30, choices=JORNADA_CHOICES, null=True)


    modalidade = models.CharField('Local', max_length=10, choices=MODALIDADE_CHOICES, null=True)
    
    
    salario = models.IntegerField(verbose_name='Salário desejado', null=True)
    
    
    habilidades = models.ManyToManyField(Habilidades)
    
    
    usuario = models.OneToOneField(User, on_delete=models.PROTECT)

    
    class Meta:
        verbose_name = 'Curriculo'
        verbose_name_plural = 'Curriculos'


    
    def __str__(self):
        return f'{self.categoria} - {self.nivel} - {self.modalidade}'

