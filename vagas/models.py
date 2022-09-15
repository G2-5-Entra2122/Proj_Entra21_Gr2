from django.db import models

class Vaga(models.Model):
    nome=models.CharField('Nome da Vaga',max_length=100)
    empregador=models.CharField('Empregador',max_length=100)
    NIVEIS_CHOICES=[
        ('Junior','Junior'),
        ('Pleno','Pleno'),
        ('Sênior','Sênior')
    ]
    nivel=models.CharField('Nível da Vaga',choices=NIVEIS_CHOICES)
    descricao=models.CharField('Descrição da vaga')
    MODALIDADES_CHOICES=[
        ('Presencial','Presencial'),
        ('Híbrido','Híbrido'),
        ('Remoto','Remoto')
    ]
    tipo_contrato=models.CharField('Modalidade da Vaga',choices=MODALIDADES_CHOICES)
    local=models.CharField('Local da Vaga')
    SN_CHOICES=[
        ('S','Sim'),
        ('N','Não')
    ]
    outras_reg=models.CharField('Aceita candidatos de outras regiões?',choices=SN_CHOICES)
    requisitos=models.CharField('Requisitos')
    habil_obr=models.CharField('Habilidade')
    salmin=models.DecimalField('Salário Mínimo',decimal_places=2)
    salmax=models.DecimalField('Salário Máximo',decimal_places=2)
    beneficios=models.CharField('Benefícios')

    class Meta:
        verbose_name = 'Vaga'
        verbose_name_plural = 'Vagas'
    
    def __str__(self):
        return f'{self.nome} ({self.nivel})'
