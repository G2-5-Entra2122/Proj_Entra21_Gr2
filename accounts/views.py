from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import Group
from .forms import CandidatoForm, EmpresaForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .models import PerfilCandidatos, PerfilEmpresas

class CandidatoCreate(CreateView):
    template_name = 'registration/register.html'
    form_class = CandidatoForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):

        grupo = get_object_or_404(Group, name="Candidato")
        
        url = super().form_valid(form)
        
        self.object.groups.add(grupo)
        self.object.save()

        PerfilCandidatos.objects.create(usuario=self.object)

        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Registro do candidato'
        return context


class EmpresaCreate(CreateView):
    template_name = 'registration/register.html'
    form_class = EmpresaForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):

        grupo = get_object_or_404(Group, name="Empresa")
        
        url = super().form_valid(form)
        
        self.object.groups.add(grupo)
        self.object.save()

        PerfilEmpresas.objects.create(usuario=self.object)

        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Registro da empresa'
        return context


class PerfilCandidatoUpdateView(UpdateView):
    model = PerfilCandidatos
    fields = ['nome', 'sobrenome', 'cpf', 'cep', 'data_nasc', 'github', 'linkedin', 'facebook', 'instagram', 'descricao']
    template_name = 'registration/register.html' 
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        # Define que apenas o usuario que criou o Form, pode editar-lo e se não for envia o usuario pra uma página 404.
        self.object = get_object_or_404(PerfilCandidatos, usuario=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Meus dados pessoais'
        return context


class PerfilEmpresaUpdateView(UpdateView):
    model = PerfilEmpresas
    fields = ['fantasia', 'razao_social', 'cnpj', 'ie', 'endereco', 'tamanho', 'ramo', 'cep', 'telefone', 'apresentacao']
    template_name = 'registration/register.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        # Define que apenas o usuario que criou o Form, pode editar-lo e se não for envia o usuario pra uma página 404.
        self.object = get_object_or_404(PerfilEmpresas, usuario=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Dados da empresa'
        return context