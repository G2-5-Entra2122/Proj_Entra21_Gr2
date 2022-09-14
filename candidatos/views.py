from django.views.generic.edit import CreateView
from .models import Candidatos, Curriculo, Habilidades
from django.urls import reverse_lazy


class CandidatosCreateView(CreateView):
    model = Candidatos
    fields = ['nome', 'sobrenome', 'cpf', 'cep', 'data_nasc', 'github', 'linkedin', 'facebook', 'instagram', 'descricao']    
    template_name = 'candidatos/form.html'
    login_url = reverse_lazy('login') 
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Perfil'
        return context    
class CurriculoCreateView(CreateView):
    model = Curriculo
    fields = [
        'perfil',
        'nivel',
        'contrato',
        'local',
        'salario',
    ]
    template_name = 'candidatos/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Curriculo'
        return context


class HabilidadesCreateView(CreateView):
    model = Habilidades
    fields = [
        'habilidade',
        'experiencia',
    ]
    template_name = 'candidatos/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Habilidades'
        return context
