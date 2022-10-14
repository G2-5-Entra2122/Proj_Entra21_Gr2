# Generated by Django 4.1.1 on 2022-10-14 12:30
from accounts.models import PerfilEmpresas
from django.db import models, migrations


def apply_migration(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Group.objects.bulk_create([
        Group(name=u'Candidato'),
        Group(name=u'Empresa')
    ])


def revert_migration(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Group.objects.filter(
        name__in=[
            u'Candidato',
            u'Empresa'
        ]
    ).delete()


# def criar_empresa(apps, schema_editor):
#     Empresa = apps.get_model('auth', 'Group')
#     PerfilEmpresas.objects.create(fantasia = 'Senior',
#      razao_social = 'Senior Sistemas', 
#      cnpj = '80.680.093/0001-81', 
#      ie = '123456789', 
#      endereco = 'Rua da Esperanca', 
#      tamanho = 'pequena', 
#      ramo = 'tecnologia', 
#      cep = '88340-080', 
#      telefone = '(47)3733-2747', 
#      apresentacao = 'ola sou a senior',
#      usuario = ''
#     )

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(apply_migration, revert_migration)
    ]

