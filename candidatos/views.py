from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from .models import Candidatos, Curriculo, Habilidades
from .forms import HabilidadesForm, CandidatosForm




################## CREATEVIEW ##################


class CandidatosCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    form_class = CandidatosForm 
    template_name = 'candidatos/form.html' 
    success_url = reverse_lazy('index')

    def form_valid(self, form):

        form.instance.usuario = self.request.user

        url = super().form_valid(form)
        
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Perfil'
        return context    


class CurriculoCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Curriculo
    fields = ['perfil', 'nivel', 'contrato', 'local', 'salario']
    template_name = 'candidatos/form.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):

        form.instance.usuario = self.request.user

        url = super().form_valid(form)
        
        return url


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Curriculo'
        return context



class HabilidadesCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    form_class = HabilidadesForm
    template_name = 'candidatos/form.html'
    success_url = reverse_lazy('candidato/habilidades')
    todas_habilidades = Habilidades.objects.all()
    
    def form_valid(self, form):

        form.instance.usuario = self.request.user

        url = super().form_valid(form)
        
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Habilidades'
        context['habilidades'] = self.todas_habilidades
        return context



################## UPDATEVIEW ##################

class CandidatosUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Candidatos
    fields = ['nome', 'sobrenome', 'cpf', 'cep', 'data_nasc', 'github', 'linkedin', 'facebook', 'instagram', 'descricao']
    template_name = 'candidatos/form.html' 
    success_url = reverse_lazy('index')


class CurriculosUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Curriculo
    fields = ['perfil', 'nivel', 'contrato', 'local', 'salario']
    template_name = 'candidatos/form.html'
    success_url = reverse_lazy('index')


class HabilidadesUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    form_class = HabilidadesForm
    template_name = 'candidatos/form.html'
    success_url = reverse_lazy('index')
    todas_habilidades = Habilidades.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['habilidades'] = self.todas_habilidades
        return context


################## LISTVIEW ##################

class CandidatoListView(ListView):
    model = Candidatos
    template_name = 'candidatos/listas/candidato.html'


class CurrucloListView(ListView):
    model = Curriculo
    template_name = 'candidatos/listas/curriculo.html'