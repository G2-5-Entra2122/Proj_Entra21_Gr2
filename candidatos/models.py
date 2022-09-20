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
    habilidade = models.CharField('Habilidade', max_length=15, choices=HABILIDADES_CHOICES)
    
    EXPERIENCIA_CHOICES = [
        ('0-1-anos', '0-1 anos'),
        ('1-2-anos', '1-2 anos'),
        ('2-3-anos', '2-3 anos'),
        ('3-4-anos', '3-4 anos'),
        ('4-5-anos', '4-5 anos'),
        ('5+-anos', '5+ anos')
    ]
    experiencia = models.CharField('Tempo de experiência', max_length=15, choices=EXPERIENCIA_CHOICES, blank=False, default='Unspecified')

    class Meta:
        verbose_name = 'Habilidade'
        verbose_name_plural = 'Habilidades'

    def __str__(self):
        return f'{self.habilidade}({self.experiencia})'



class Curriculo(models.Model):
    PERFIL_CHOICES = (
        ('full_stack', 'Full-Stack'),
        ('fron_end', 'Front-End'),
        ('back_end', 'Back-End'),
        ('mobile', 'Mobile'),
    )
    perfil = models.CharField('Área', max_length=10, choices=PERFIL_CHOICES)    
    
    NIVEL_CHOICES = (
        ('senior', 'Sênior'),
        ('pleno', 'Pleno'),
        ('junior', 'Junior'),
        )
    nivel = models.CharField('Nível', max_length=6, choices=NIVEL_CHOICES)
    
    CONTRATO_CHOICES = (
        ('estagio', 'Estágio'),
        ('pj', 'PJ'),
        ('clt', 'CLT'),
    )
    contrato = models.CharField('Contrato', max_length=7, choices=CONTRATO_CHOICES)

    LOCAL_CHOICES = (
        ('presencial', 'Presencial'),
        ('hibrido', 'Híbrido'),
        ('remoto', 'Remoto'),
    )
    local = models.CharField('Local', max_length=10, choices=LOCAL_CHOICES)
    salario = models.IntegerField(verbose_name='Salário desejado')
    habilidades = models.ManyToManyField(Habilidades)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Curriculo'
        verbose_name_plural = 'Curriculos'


    def __str__(self):
        return f'{self.perfil} - {self.nivel} - {self.local}'

