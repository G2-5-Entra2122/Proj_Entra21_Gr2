from django.db import models
from django.contrib.auth.models import User

class Habilidade(models.Model):

    habilidade = models.CharField('Habilidade', max_length=50,  null=True, blank=True)

    class Meta:
        verbose_name = 'Habilidade'
        verbose_name_plural = 'Habilidades'


    def __str__(self):
        return f'{self.habilidade}'



class Curriculo(models.Model):
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
    contrato = models.CharField('Contrato', max_length=10, choices=CONTRATO_CHOICES, null=True)


    MODALIDADE_CHOICES = (
        ('Presencial','Presencial'),
        ('Híbrido','Híbrido'),
        ('Remoto','Remoto')
    )
    modalidade = models.CharField('Local', max_length=10, choices=MODALIDADE_CHOICES, null=True)


    salario = models.IntegerField(verbose_name='Salário desejado', null=True)


    pri_habilidade_candidato = models.ForeignKey(Habilidade, verbose_name='1ª - Habilidade', related_name='pri_habilidade_candidato+', null=True, on_delete=models.PROTECT)
    seg_habilidade_candidato = models.ForeignKey(Habilidade, verbose_name='2ª - Habilidade', related_name='seg_habilidade_candidato+', null=True, blank=True, on_delete=models.PROTECT)
    ter_habilidade_candidato = models.ForeignKey(Habilidade, verbose_name='3ª - Habilidade', related_name='ter_habilidade_candidato+', null=True, blank=True, on_delete=models.PROTECT)
    qua_habilidade_candidato = models.ForeignKey(Habilidade, verbose_name='4ª - Habilidade', related_name='qua_habilidade_candidato+', null=True, blank=True, on_delete=models.PROTECT)
    qui_habilidade_candidato = models.ForeignKey(Habilidade, verbose_name='5ª - Habilidade', related_name='qui_habilidade_candidato+', null=True, blank=True, on_delete=models.PROTECT)


    usuario = models.OneToOneField(User, on_delete=models.PROTECT)


    class Meta:
        verbose_name = 'Curriculo'
        verbose_name_plural = 'Curriculos'


    def __str__(self):
        return f'{self.categoria} - {self.nivel} - {self.modalidade}'
