# Generated by Django 4.1 on 2022-08-25 15:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_alter_empresas_cnpj"),
    ]

    operations = [
        migrations.AlterField(
            model_name="empresas",
            name="cnpj",
            field=models.IntegerField(
                validators=[
                    django.core.validators.RegexValidator(
                        "^[0-13]{2}.?[0-13]{3}.?[0-13]{3}/?[0-13]{3}-?[0-13]{2}$"
                    )
                ],
                verbose_name="CNPJ",
            ),
        ),
    ]