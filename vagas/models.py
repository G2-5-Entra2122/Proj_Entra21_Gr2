from django.db import models

class Vaga(models.Model):
    nome=models.CharField('Nome da Vaga',max_length=100)
    empregador=models.CharField('Empregador',max_length=100)
    niveis=[
        'Junior',
        'Pleno',
        'Sênior'
    ]
    nivel=models.CharField('Nível da Vaga',choices=niveis)
    descricao=models.CharField('Descrição da vaga')
    modalidades=[
        'Presencial',
        'Híbrido',
        'Remoto'
    ]
    tipo_contrato=models.CharField('Modalidade da Vaga',choices=modalidades)
    local=models.CharField('Local da Vaga')
    sncheck=[
        'Sim',
        'Não'
    ]
    outras_reg=models.CharField('Aceita candidatos de outras regiões?',choices=sncheck)
    requisitos=models.CharField('Requisitos')
    habil_obr=models.CharField('Habilidade')
    salmin=models.DecimalField('Salário Mínimo',decimal_places=2)
    salmax=models.DecimalField('Salário Máximo',decimal_places=2)
    beneficios=models.CharField('Benefícios')
