from requests import request
from .models import Vaga

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .forms import FilterForm



######################## CREATE ##########################


class VagaCreateView(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required= u'Empresa'
    login_url=reverse_lazy('login')
    model = Vaga
    fields=[
            'nome',
            'categoria',
            'nivel',
            'descricao',
            'modalidade',
            'contrato',
            'jornada',
            'local',
            'outras_reg',
            'requisitos',
            'salmin',
            'salmax',
            'beneficios',
            'pri_habilidade_vaga',
            'seg_habilidade_vaga',
            'ter_habilidade_vaga',
            'qua_habilidade_vaga',
            'qui_habilidade_vaga',
        ]
    # form_class=VagasForm
    # vagas_obj=Vaga.objects.all()
    template_name = 'vagas/form.html'
    success_url=reverse_lazy('minhas-vagas')

    def form_valid(self, form):
        form.instance.usuario=self.request.user

        url = super().form_valid(form)
        
        return url


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Adicionar uma vaga'
        context['lead'] = 'Preencha todos os campos obrigatórios.'
        context['botao'] = 'Cadastrar'
        return context



######################## LIST ##########################


class MinhasVagasListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = u'Empresa'
    login_url = reverse_lazy('login')
    model = Vaga
    fields=[
            'nome',
            'categoria',
            'nivel',
            'descricao',
            'modalidade',
            'contrato',
            'jornada',
            'local',
            'outras_reg',
            'requisitos',
            'salmin',
            'salmax',
            'beneficios',
            'pri_habilidade_vaga',
            'seg_habilidade_vaga',
            'ter_habilidade_vaga',
            'qua_habilidade_vaga',
            'qui_habilidade_vaga',
        ]
    template_name = 'vagas/minhasvagas.html'
    

    def get_queryset(self):
        self.object_list = Vaga.objects.filter(usuario=self.request.user)
        return self.object_list
 

class VagaListView(ListView):
    template_name='vagas/vagas-list.html'
    model = Vaga
    
    def get_queryset(self):
        vagas = Vaga.objects.all()        
        search_001 = self.request.GET.get('search-001')
        if search_001:
            if search_001 != "Todas as categorias":
                vagas = vagas.filter(categoria=search_001)
            elif search_001 == "Todas as categorias":
                vagas=vagas.objects.all()    

        search_002 = self.request.GET.get('search-002')
        if search_002:
            if search_002 != "Todos os niveis":
                vagas = vagas.filter(nivel=search_002)
            elif search_002 == "Todos os niveis":
                vagas=vagas.objects.all()

        search_003 = self.request.GET.get('search-003')
        if search_003:
            if search_003 != "Todas as modalidades":
                vagas = vagas.filter(modalidade=search_003)
            elif search_003 == "Todas as modalidades":
                vagas=vagas.objects.all()

        search_004 = self.request.GET.get('search-004')
        if search_004:
            if search_004 != "Tipo de contrato":
                vagas = vagas.filter(contrato=search_004)
            elif search_004 == "Tipo de contrato":
                vagas=vagas.objects.all()

        search_005 = self.request.GET.get('search-005')
        if search_005:
            if search_005 != "Tipo de jornada":
                vagas = vagas.filter(jornada=search_005)
            elif search_005 == "Tipo de jornada":
                vagas=vagas.objects.all()

        search_006 = self.request.GET.get('search-006')
        if search_006:
            if search_005 != "Aceita outra região?":
                vagas = vagas.filter(outras_reg=search_006)
            elif search_006 == "Aceita outra região?":
                vagas=vagas.objects.all()

        return vagas

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['form'] = FilterForm(initial={
            'search': self.request.GET.get('search', ''),
            'filter_field': self.request.GET.get('filter_field', '')
        })
        return context



######################## ALTERAR ##########################


class VagaUpdateView(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u'Empresa'
    login_url = reverse_lazy('login')
    model = Vaga
    fields=[
            'nome',
            'categoria',
            'nivel',
            'descricao',
            'modalidade',
            'contrato',
            'jornada',
            'local',
            'outras_reg',
            'requisitos',
            'salmin',
            'salmax',
            'beneficios',
            'pri_habilidade_vaga',
            'seg_habilidade_vaga',
            'ter_habilidade_vaga',
            'qua_habilidade_vaga',
            'qui_habilidade_vaga',
        ]
    template_name = 'vagas/form.html'
    success_url = reverse_lazy('minhas-vagas')

    def get_object(self, queryset=None):
        # self.object = Vaga.objects.get(pk=self.kwargs['pk'], usuario=self.request.user)
        self.object = get_object_or_404(Vaga, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Atualizar vaga'
        context['lead'] = 'Preencha todos os campos obrigatórios.'
        context['botao'] = 'Atualizar'
        return context
     
        
######################## DELETE ##########################


class MinhasVagasDeleteView(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u'Empresa'
    model = Vaga
    template_name ='vagas/form-excluir.html'
    success_url = reverse_lazy('minhas-vagas')

    def get_object(self, queryset=None):
        # self.object = Vaga.objects.get(pk=self.kwargs['pk'], usuario=self.request.user)
        self.object = get_object_or_404(Vaga, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Deletar vaga'
        context['lead'] = 'Confirme para excluir a vaga definitivamente.'
        context['botao'] = 'Deletar'
        return context




