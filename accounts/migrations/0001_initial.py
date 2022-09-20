# Generated by Django 4.1.1 on 2022-09-20 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PerfilEmpresas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fantasia', models.CharField(max_length=100, null=True, verbose_name='Nome Fantasia')),
                ('razao_social', models.CharField(max_length=100, null=True, verbose_name='Razão Social')),
                ('cnpj', models.CharField(max_length=18, null=True, verbose_name='CNPJ')),
                ('ie', models.CharField(blank=True, max_length=20, null=True, verbose_name='Inscrição Estadual')),
                ('endereco', models.CharField(max_length=100, null=True, verbose_name='Endereço')),
                ('tamanho', models.CharField(choices=[('pequena', 'Pequena'), ('media', 'Média'), ('grande', 'Grande')], max_length=7, null=True, verbose_name='Tamanho')),
                ('ramo', models.CharField(choices=[('tecnologia', 'Tecnologia'), ('servicos', 'Serviços'), ('financeiro', 'Financeiro'), ('varejo', 'Varejo'), ('atacado', 'Atacado'), ('industria', 'Industria'), ('comercio', 'Comércio')], max_length=50, null=True, verbose_name='Ramo')),
                ('cep', models.CharField(max_length=9, null=True, verbose_name='CEP')),
                ('telefone', models.CharField(max_length=15, null=True, verbose_name='Telefone')),
                ('apresentacao', models.TextField(max_length=500, verbose_name='Apresentação')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
        ),
        migrations.CreateModel(
            name='PerfilCandidatos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, null=True, verbose_name='Nome')),
                ('sobrenome', models.CharField(max_length=50, null=True, verbose_name='Sobrenome')),
                ('cpf', models.CharField(max_length=14, null=True, verbose_name='CPF')),
                ('cep', models.CharField(max_length=9, null=True, verbose_name='CEP')),
                ('data_nasc', models.DateField(max_length=10, null=True, verbose_name='Data de Nascimento')),
                ('github', models.CharField(default='#', max_length=100, verbose_name='GitHub')),
                ('linkedin', models.CharField(default='#', max_length=100, verbose_name='Linkedin')),
                ('facebook', models.CharField(default='#', max_length=100, verbose_name='Facebook')),
                ('instagram', models.CharField(default='#', max_length=100, verbose_name='Instagram')),
                ('descricao', models.TextField(max_length=200, null=True, verbose_name='Descrição')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]