from django.db import models


class EmpresaTamanho(models.Model):
    tamanho = models.CharField('Tamanho da Empresa', max_length=100)

    class Meta:
        verbose_name = 'Tamanho da empresa'
        verbose_name_plural = 'Tamanho da empresas'

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
    cnpj = models.CharField('CNPJ', max_length=18)
    endereco = models.CharField('Endereço', max_length=100)
    tamanho = models.ForeignKey('app.EmpresaTamanho', verbose_name='Tamanho', on_delete=models.CASCADE)
    ramo = models.ForeignKey('app.EmpresaRamo', verbose_name='Ramo da empresa', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.razao_social
    
