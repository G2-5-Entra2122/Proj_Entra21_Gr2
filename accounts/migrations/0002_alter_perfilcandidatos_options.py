from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='perfilcandidatos',
            options={'verbose_name': 'Candidato', 'verbose_name_plural': 'Candidatos'},
        ),
    ]
