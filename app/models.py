
from django.db import models


class EmpresaTamanho(models.Model):
    tamanho = models.CharField('Tamanho da Empresa', max_length=100)

    class Meta:
        verbose_name = 'Tamanho da empresa'
        verbose_name_plural = 'Tamanho das empresas'

    def __str__(self):
        return self.tamanho
        
class EmpresaRamo(models.Model):
    ramo = models.CharField('Ramo da empresa', max_length=100)

    class Meta:
        verbose_name = 'Ramo da empresa'
        verbose_name_plural = 'Ramo das empresas'

    def __str__(self):
        return self.ramo


class Empresas(models.Model):
    razao_social = models.CharField('Razão Social', max_length=100)
    cnpj = models.CharField('CNPJ', max_length=14)
    endereco = models.CharField('Endereço', max_length=100)
    tamanho = models.ForeignKey('app.EmpresaTamanho', verbose_name='Tamanho', on_delete=models.CASCADE)
    ramo = models.ForeignKey('app.EmpresaRamo', verbose_name='Ramo da empresa', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.razao_social
    #telefone, senha, confirma senha, tamanho/porte da empresa; inscrição estadual (se tiver); tamanho/porte; campo para logo da empresa; campo para história da empresa

class Pessoas(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    cpf = models.CharField('CPF', max_length=11)
    endereco = models.CharField('Endereco', max_length=100)
    data_nasc = models.CharField('Data de Nascimento', max_length=10)
    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        abstract = True

    def __str__(self):
        return self.nome
    
    #e-mail, telefone, linkedin, github, facebook, instagram, apresente-se (campo para pessoa escrever sobre ela mesma) e botão salvar


class Nivel(models.Model):
    nome = models.CharField('Nome', max_length=100)

    class Meta:
        verbose_name = 'Nivel'
        verbose_name_plural = 'Niveis'

    def __str__(self):
        return self.nome


class Area(models.Model):
    nome = models.CharField('Nome', max_length=100)

    class Meta:
        verbose_name = 'Area'
        verbose_name_plural = 'Areas'

    def __str__(self):
        return self.nome


class Habilidades(models.Model):
    nome = [
        ('py', 'Python'),
        ('js', 'JavaScript'),
        ('ts', 'TypeScript'),
        ('dj', 'Django'),
        ('php', 'PHP')
    ]
    habilidades = models.CharField('Habilidade', max_length=15, choices=nome)
    
    experiencia = [
        ('0-1-anos', '0-1 anos'),
        ('1-2-anos', '1-2 anos'),
        ('2-3-anos', '2-3 anos'),
        ('3-4-anos', '3-4 anos'),
        ('4-5-anos', '4-5 anos'),
        ('5+-anos', '5+ anos')
    ]
    tempo = models.CharField('Tempo', max_length=15, choices=experiencia, blank=False, default='Unspecified')

    class Meta:
        ordering = ['habilidades']
        verbose_name = 'Habilidade'
        verbose_name_plural = 'Habilidades'

    def __str__(self):
        return self.nome


class Candidato(Pessoas):
    perfil_linkedin = models.CharField('Linkedin', max_length=100)
    nivel = models.ForeignKey('app.Nivel', verbose_name='Nivel', on_delete=models.CASCADE)
    area = models.ForeignKey('app.Area', verbose_name='Area', on_delete=models.CASCADE)
    habilidades = models.ManyToManyField(Habilidades)

    class Meta:
        ordering = ['area']
        verbose_name = 'Candidato'
        verbose_name_plural = 'Candidatos'

    def __str__(self):
        return self.nome
    #titulo do curriculo, local da vaga (presencial, hibrido ou remoto), objetivo (full/front/back), nivel de experiência (geral), habilidades (já esta aqui/ mais tempo de habilidade por linguagem), experiencias (inicio, fim, cargo, descrição), 
    #o que você busca {[tipo de contrato pj/clt/estagio]; faixa salarial; porte da empresa (em discussao se coloca ou nao)}