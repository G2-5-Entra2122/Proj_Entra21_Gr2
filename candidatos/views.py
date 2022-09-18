from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import get_object_or_404
# from django.views.generic.list import ListView

from .models import Curriculo, Habilidades
from .forms import HabilidadesForm




################## CREATEVIEW ##################


class CurriculoCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Curriculo
    fields = ['perfil', 'nivel', 'contrato', 'local', 'salario']
    template_name = 'candidatos/form.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        # Define o atributo usuario, como o usuario que está logado.
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
        # Define o atributo usuario, como o usuario que está logado.
        form.instance.usuario = self.request.user

        url = super().form_valid(form)
        
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs )

        context['titulo'] = 'Habilidades'
        context['habilidades'] = self.todas_habilidades
        return context



################## UPDATEVIEW ##################





class CurriculosUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Curriculo
    fields = ['perfil', 'nivel', 'contrato', 'local', 'salario']
    template_name = 'candidatos/form.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        # Define que apenas o usuario que criou o Form, pode editar-lo e se não for envia o usuario pra uma página 404.
        self.object = get_object_or_404(Curriculo, pk=self.kwargs['pk'], usuario=self.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Meus curriculo'


class HabilidadesUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    form_class = HabilidadesForm
    template_name = 'candidatos/form.html'
    success_url = reverse_lazy('index')
    todas_habilidades = Habilidades.objects.all()

    def get_object(self, queryset=None):
        # Define que apenas o usuario que criou o Form, pode editar-lo e se não for envia o usuario pra uma página 404.
        self.object = get_object_or_404(Habilidades, pk=self.kwargs['pk'], usuario=self.user)
        return self.object



################## LISTVIEW ##################

# class CandidatoListView(ListView):
#     model = Candidatos
#     template_name = 'candidatos/listas/candidato.html'
    # def get_queryset(self):
    #     self.object_list = Candidatos.objects.filter(usuario=self.request.user)
    #     return self.objeto_list


# class CurriculoListView(ListView):
#     model = Curriculo
#     template_name = 'candidatos/listas/curriculo.html'