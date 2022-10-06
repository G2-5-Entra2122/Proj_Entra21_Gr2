from django.db import models


class Vaga(models.Model):
    nome=models.CharField('Nome da Vaga',max_length=100)
    empregador=models.CharField('Empregador',max_length=100)
    NIVEIS_CHOICES=[
        ('Junior','Junior'),
        ('Pleno','Pleno'),
        ('Sênior','Sênior')
    ]
    nivel=models.CharField('Nível da Vaga',choices=NIVEIS_CHOICES,max_length=6)
    descricao=models.TextField('Descrição da vaga',max_length=500)
    MODALIDADES_CHOICES=[
        ('Presencial','Presencial'),
        ('Híbrido','Híbrido'),
        ('Remoto','Remoto')
    ]
    tipo_contrato=models.CharField('Modalidade da Vaga',choices=MODALIDADES_CHOICES,max_length=10)
    local=models.CharField('Local da Vaga',max_length=30)
    SN_CHOICES=[
        ('Sim','Sim'),
        ('Não','Não')
    ]
    outras_reg=models.CharField('Aceita candidatos de outras regiões?',choices=SN_CHOICES,max_length=3)
    requisitos=models.CharField('Requisitos',max_length=50)
    habil_obr=models.CharField('Habilidade',max_length=30)
    salmin=models.DecimalField('Salário Mínimo',decimal_places=2,max_digits=10)
    salmax=models.DecimalField('Salário Máximo',decimal_places=2,max_digits=10)
    beneficios=models.TextField('Benefícios',max_length=500)

    class Meta:
        verbose_name = 'Vaga'
        verbose_name_plural = 'Vagas'
    
    def __str__(self):
        return f'{self.nome} ({self.nivel})'
