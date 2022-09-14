from django.views.generic.edit import CreateView
from .models import Candidatos, Curriculo, Habilidades
from .forms import HabilidadesForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class CandidatosCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Candidatos
    fields = ['nome', 'sobrenome', 'cpf', 'cep', 'data_nasc', 'github', 'linkedin', 'facebook', 'instagram', 'descricao']    
    template_name = 'candidatos/form.html'
    login_url = reverse_lazy('login') 
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Perfil'
        return context    


class CurriculoCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
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


class HabilidadesCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    form_class = HabilidadesForm

    template_name = 'candidatos/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Habilidades'
        return context
