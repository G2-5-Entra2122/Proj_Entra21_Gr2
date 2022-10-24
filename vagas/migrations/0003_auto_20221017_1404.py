# Generated by Django 4.1.1 on 2022-10-17 17:04

from django.db import migrations
from django.contrib.auth.models import User


def add_users(apps,schema_editor):
    DEFAULT_USERS =[
        ('ambevtech','contato@ambevtech.com.br','@Empresa123'),
        ('ailos','contato@ailos.com.br', '@Empresa123'),
        ('capgemini', 'contato@capgemini.com.br', '@Empresa123'),
        ('datainfo', 'contato@datainfo.com.br', '@Empresa123'),
        ('farmaciasapp','contato@farmaciasapp.com.br', '@Empresa123'),
        ('havanlabs', 'contato@havanlabs.com.br', '@Empresa123'),
        ('philips','contato@philips.com.br','@Empresa123'),
        ('senior','contato@seniorsistemas.com.br','@Empresa123'),
        ('tsystems', 'contato@tsystems.com.br','@Empresa123'),
        ('unifique', 'contato@unifique.com.br', '@Empresa123'),
        ('warren', 'contato@warren.com.br', '@Empresa123'),
        ('raquel','raquel@raquel.com.br','@Candidato123'),
        ('mark','mark@mark.com.br','@Candidato123'),
        ('nicolas','nicolas@nicolas.com.br','@Candidato123'),
        ('luiza','luiza@luiza.com.br','@Candidato123'),
        ('diego','diego@diego.com.br', '@Candidato123'),
        ('felipe', 'felipe@felipe.com.br', '@Candidato123'),
        ('jose','jose@jose.com.br','@Candidato123'),
        ('joao','joao@joao.com.br','@Candidato123')
        ]
    for username, email, password in DEFAULT_USERS:
        user = User.objects.create_user(username, email, password)
        user.groups.add(2)
        user.save()

#def remove_users(apps,schema_editor):



class Migration(migrations.Migration):

    dependencies = [
        ('vagas', '0002_auto')
    ]

    operations = [
        migrations.RunPython(add_users, add_users )
    ]