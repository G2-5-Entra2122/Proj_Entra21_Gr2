
from django.db.models import F, When, Value, Q, Count, ExpressionWrapper, Case
from django.db import models
from candidatos.models import Curriculo
from .models import Vaga

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404



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
    template_name='vagas/vaga_list.html'
    model=Vaga



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



######################## DETAIL ##########################


class MinhaVagaDetailView(GroupRequiredMixin, LoginRequiredMixin, DetailView):
    group_required = u'Empresa'
    model = Vaga
    template_name = 'vagas/vaga-detail.html'
    context_object_name = 'vaga'

    def get_object(self, queryset=None):
        # self.object = Vaga.objects.get(pk=self.kwargs['pk'], usuario=self.request.user)
        self.object = get_object_or_404(Vaga, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        vaga = self.object
        # vaga.categoria='back_end'
        # vaga.nivel='pleno'
        qs = Curriculo.objects.filter(nivel=vaga.nivel)
        
        
        exp = Case(
            When(categoria__exact=vaga.categoria, then=10),
            default=0, 
            output_field=models.IntegerField()
            )
        exp += Case(
            When(modalidade__exact=vaga.modalidade, then=10),
            default=0, 
            output_field=models.IntegerField()
            )
        exp += Case(
            When(contrato__exact=vaga.contrato, then=10),
            default=0, 
            output_field=models.IntegerField()
            )

        # Candidato Primeira Habildiade    

        exp += Case(
            When(pri_habilidade_candidato__exact=vaga.pri_habilidade_vaga, then=10),
            default=0, 
            output_field=models.IntegerField()
            )
        exp += Case(
            When(pri_habilidade_candidato__exact=vaga.seg_habilidade_vaga, then=10),
            default=0, 
            output_field=models.IntegerField()
            )
        exp += Case(
            When(pri_habilidade_candidato__exact=vaga.ter_habilidade_vaga, then=10),
            default=0, 
            output_field=models.IntegerField()
            )
        exp += Case(
            When(pri_habilidade_candidato__exact=vaga.qua_habilidade_vaga, then=10),
            default=0, 
            output_field=models.IntegerField()
            )
        exp += Case(
            When(pri_habilidade_candidato__exact=vaga.qui_habilidade_vaga, then=10),
            default=0, 
            output_field=models.IntegerField()
            )

        # Candidato Segunda Habildiade

        exp += Case(
            When(seg_habilidade_candidato__exact=vaga.pri_habilidade_vaga, then=10),
            default=0, 
            output_field=models.IntegerField()
            )
        exp += Case(
            When(seg_habilidade_candidato__exact=vaga.seg_habilidade_vaga, then=10),
            default=0, 
            output_field=models.IntegerField()
            )
        exp += Case(
            When(seg_habilidade_candidato__exact=vaga.ter_habilidade_vaga, then=10),
            default=0, 
            output_field=models.IntegerField()
            )
        exp += Case(
            When(seg_habilidade_candidato__exact=vaga.qua_habilidade_vaga, then=10),
            default=0, 
            output_field=models.IntegerField()
            )
        exp += Case(
            When(seg_habilidade_candidato__exact=vaga.qui_habilidade_vaga, then=10),
            default=0, 
            output_field=models.IntegerField()
            )

        # Candidato Terceira Habildiade

        exp += Case(
            When(ter_habilidade_candidato__exact=vaga.pri_habilidade_vaga, then=10),
            default=0, 
            output_field=models.IntegerField()
            )
        exp += Case(
            When(ter_habilidade_candidato__exact=vaga.seg_habilidade_vaga, then=10),
            default=0, 
            output_field=models.IntegerField()
            )
        exp += Case(
            When(ter_habilidade_candidato__exact=vaga.ter_habilidade_vaga, then=10),
            default=0, 
            output_field=models.IntegerField()
            )
        exp += Case(
            When(ter_habilidade_candidato__exact=vaga.qua_habilidade_vaga, then=10),
            default=0, 
            output_field=models.IntegerField()
            )
        exp += Case(
            When(ter_habilidade_candidato__exact=vaga.qui_habilidade_vaga, then=10),
            default=0, 
            output_field=models.IntegerField()
            )

        # Candidato Quarta Habildiade

        exp += Case(
            When(qua_habilidade_candidato__exact=vaga.pri_habilidade_vaga, then=10),
            default=0, 
            output_field=models.IntegerField()
            )
        exp += Case(
            When(qua_habilidade_candidato__exact=vaga.seg_habilidade_vaga, then=10),
            default=0, 
            output_field=models.IntegerField()
            )
        exp += Case(
            When(qua_habilidade_candidato__exact=vaga.ter_habilidade_vaga, then=10),
            default=0, 
            output_field=models.IntegerField()
            )
        exp += Case(
            When(qua_habilidade_candidato__exact=vaga.qua_habilidade_vaga, then=10),
            default=0, 
            output_field=models.IntegerField()
            )
        exp += Case(
            When(qua_habilidade_candidato__exact=vaga.qui_habilidade_vaga, then=10),
            default=0, 
            output_field=models.IntegerField()
            )

        # Candidato Quinta Habildiade

        exp += Case(

            When(qui_habilidade_candidato__exact=vaga.pri_habilidade_vaga, then=10),
            default=0, 
            output_field=models.IntegerField()
            )
        exp += Case(
            
            When(qui_habilidade_candidato__exact=vaga.seg_habilidade_vaga, then=10),
            default=0, 
            output_field=models.IntegerField()
            )
        exp += Case(
            
            When(qui_habilidade_candidato__exact=vaga.ter_habilidade_vaga, then=10),
            default=0, 
            output_field=models.IntegerField()
            )
        exp += Case(
            
            When(qui_habilidade_candidato__exact=vaga.qua_habilidade_vaga, then=10),
            default=0, 
            output_field=models.IntegerField()
            )
        exp += Case(
            
            When(qui_habilidade_candidato__exact=vaga.qui_habilidade_vaga, then=10),
            default=0, 
            output_field=models.IntegerField()
            )


        if vaga.categoria != 'Mobile':
            exp += Case(
                When(categoria__exact='full_stack', then=10),
                default=0, 
                output_field=models.IntegerField()
                )

        # qs = qs.filter(categoria='full_stack').annotate(pontos=1)
        # qs = qs | qs.filter(Q(categoria__exact=Value(vaga.categoria))).annotate(pontos=F('pontos')+1)        

        # exp = models.Value(models.F('categoria') == vaga.categoria)
        # qs = qs.annotate(pontos=models.Value(vaga.categoria, output_field=models.CharField()))
        qs = qs.annotate(pontos=exp) 
        # qs = qs.filter(pontos = 10).values()
        qs = qs.values()
        context['curriculo'] = qs
        return context