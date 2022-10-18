from django.forms import Form, CharField, ChoiceField


class FilterForm(Form):
    CATEGORIA_CHOICES = (
        ('Full-stack', 'Full-Stack'),
        ('Front-end', 'Front-end'),
        ('Back-end', 'Back-end'),
        ('Mobile', 'Mobile')
    )
    search = CharField(required=False)
    filter_field = ChoiceField(choices=CATEGORIA_CHOICES)

    NIVEIS_CHOICES=[
        ('Junior','Junior'),
        ('Pleno','Pleno'),
        ('Sênior','Sênior')
    ]
    search = CharField(required=False)
    filter_field = ChoiceField(choices=NIVEIS_CHOICES)

    MODALIDADES_CHOICES=[
        ('Presencial','Presencial'),
        ('Híbrido','Híbrido'),
        ('Remoto','Remoto')
    ]
    search = CharField(required=False)
    filter_field = ChoiceField(choices=MODALIDADES_CHOICES)

    CONTRATO_CHOICES = [
        ('Estágio', 'Estágio'),
        ('CLT', 'CLT'),
        ('Freelance', 'Freelance'),
        ('PJ', 'PJ'),
        ('Voluntário', 'Voluntário'),
    ]
    search = CharField(required=False)
    filter_field = ChoiceField(choices=CONTRATO_CHOICES)

    JORNADA_CHOICES = [
        ('Período Integral', 'Período Integral'),
        ('Meio Preíodo', 'Meio Período'),
    ]
    search = CharField(required=False)
    filter_field = ChoiceField(choices=JORNADA_CHOICES)

    OUTRAS_REG_CHOICES=[
        ('sim','Sim'),
        ('nao','Não')
    ]
    search = CharField(required=False)
    filter_field = ChoiceField(choices=OUTRAS_REG_CHOICES)
