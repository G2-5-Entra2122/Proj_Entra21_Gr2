from django import django_filters
from .models import Vaga


class JornadaFilter(Vaga.JORNADA_CHOICES, django_filters.FilterSet):
    jornadafilter = django_filters.ChoiceFilter(choices=Vaga.JORNADA_CHOICES)