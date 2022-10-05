
from django.db.models import F, When, Value, Q, Count, ExpressionWrapper, Case
from django.db import models
from candidatos.models import Curriculo
from .models import Vaga
from .forms import VagasForm
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404




class VagaCreateView(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required= u'Empresa'
    login_url=reverse_lazy('login')
    model=Vaga
    fields=[
            'nome',
            'nivel',
            'descricao',
            'tipo_contrato',
            'local',
            'outras_reg',
            'requisitos',
            'habil_obr',
            'salmin',
            'salmax',
            'beneficios'
        ]
    # form_class=VagasForm
    # vagas_obj=Vaga.objects.all()
    template_name='vagas/form.html'
    success_url=reverse_lazy('index')

    def form_valid(self, form):
        form.instance.usuario=self.request.user

        url = super().form_valid(form)
        
        return url


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Adicionar uma vaga'
        # context['vagas']=self.vagas_obj
        return context

class VagaUpdateView(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required= u'Empresa'
    login_url=reverse_lazy('login')
    form_class=VagasForm
    template_name='vagas/form.html'
    success_url=reverse_lazy('index')
    vagas_obj=Vaga.objects.all()

    def get_object(self, queryset: None):
        self.object=get_object_or_404(Vaga,pk=self.kwargs['pk'],usuario=self.user)
        return self.object


class VagaListView(ListView):
    template_name='vagas/vaga_list.html'
    model=Vaga

    # def get_queryset(self):
    #     lista = list(Vaga.objects.all())
    #     # Vaga.objects.update(nivel='Senior')
    #     return lista

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        vaga = Vaga.objects.first()
        # vaga.categoria='back_end'
        # vaga.nivel='pleno'
        qs = Curriculo.objects
        
        exp = Case(
            When(categoria__exact=vaga.categoria, then=5),
            default=0, 
            output_field=models.IntegerField()
            )
        exp += Case(
            When(nivel__exact=vaga.nivel, then=2),
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

"""
vaga = pk1

curriculos =  Curriculo.object.all()

for x in curriculos:
    pt = 0
    pt += abs(vaga.CATEGORIA_CHOICES.indexof(x.categoria)-vaga.CATEGORIA_CHOICES.indexof(vaga.categoria))
    lista = ['categoria', 'nivel']



"""