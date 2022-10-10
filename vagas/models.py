from django.db import models
from django.contrib.auth.models import User
from candidatos.models import Habilidade



class Vaga(models.Model):
    nome=models.CharField('Nome da Vaga',max_length=100,help_text='Exemplo: "Desenvolvedor Web"')
    
    CATEGORIA_CHOICES = (
        ('Full-stack', 'Full-Stack'),
        ('Front-end', 'Front-end'),
        ('Back-end', 'Back-end'),
        ('Mobile', 'Mobile'),
    )
    categoria = models.CharField('Categoria', max_length=10, choices=CATEGORIA_CHOICES, null=True)
    
    
    NIVEIS_CHOICES=[
        ('Junior','Junior'),
        ('Pleno','Pleno'),
        ('Sênior','Sênior')
    ]
    nivel=models.CharField('Nível da Vaga',choices=NIVEIS_CHOICES,max_length=6)
    
    
    descricao=models.TextField('Descrição da vaga',max_length=500,help_text='Resumo da vaga de emprego e funções exercidas em no máximo 500 caracteres.')
    
    
    MODALIDADES_CHOICES=[
        ('Presencial','Presencial'),
        ('Híbrido','Híbrido'),
        ('Remoto','Remoto')
    ]
    modalidade=models.CharField('Modalidade da Vaga',choices=MODALIDADES_CHOICES,max_length=10,null=True)
    
    
    CONTRATO_CHOICES = (
        ('Estágio', 'Estágio'),
        ('CLT', 'CLT'),
        ('Freelance', 'Freelance'),
        ('PJ', 'PJ'),
        ('Voluntário', 'Voluntário'),
    )
    contrato = models.CharField('Contrato', max_length=15, choices=CONTRATO_CHOICES, null=True)


    JORNADA_CHOICES = (
        ('Período Integral', 'Período Integral'),
        ('Meio Preíodo', 'Meio Período'),
    )
    jornada = models.CharField('Jornada', max_length=30, choices=JORNADA_CHOICES, null=True)


    local=models.CharField('Local da Vaga',max_length=30,help_text='Onde reside sua empresa, para vagas presenciais. Para trabalho remoto, use "Online".')

    OUTRAS_REG_CHOICES=[
        ('sim','Sim'),
        ('nao','Não')
    ]
    
    outras_reg=models.CharField('Aceita candidatos de outras regiões?',choices=OUTRAS_REG_CHOICES,max_length=3)
    
    
    requisitos=models.CharField('Requisitos',max_length=50,help_text='Exemplos: "Formação em nível superior", "Tecnólogo", etc.')
    
    salmin=models.DecimalField('Salário Mínimo',decimal_places=2,max_digits=10)
    
    salmax=models.DecimalField('Salário Máximo',decimal_places=2,max_digits=10)
     
    beneficios=models.TextField('Benefícios',max_length=500,help_text='Exemplos: "Vale refeição", "Plano de saúde", etc.')
    
    data=models.DateField('Data de criação:',auto_now_add=True)

    pri_habilidade_vaga = models.ForeignKey(Habilidade, verbose_name='1ª - Habilidade', related_name='pri_habilidade_vaga+', null=True, on_delete=models.PROTECT)
    seg_habilidade_vaga = models.ForeignKey(Habilidade, verbose_name='2ª - Habilidade', related_name='pri_habilidade_vaga+', null=True, blank=True, on_delete=models.PROTECT)
    ter_habilidade_vaga = models.ForeignKey(Habilidade, verbose_name='3ª - Habilidade', related_name='pri_habilidade_vaga+', null=True, blank=True, on_delete=models.PROTECT)
    qua_habilidade_vaga = models.ForeignKey(Habilidade, verbose_name='4ª - Habilidade', related_name='pri_habilidade_vaga+', null=True, blank=True, on_delete=models.PROTECT)
    qui_habilidade_vaga = models.ForeignKey(Habilidade, verbose_name='5ª - Habilidade', related_name='pri_habilidade_vaga+', blank=True, on_delete=models.PROTECT)


    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    
    class Meta:
        verbose_name = 'Vaga'
        verbose_name_plural = 'Vagas'
    
    
    def __str__(self):
        return f'{self.nome} ({self.nivel})'
