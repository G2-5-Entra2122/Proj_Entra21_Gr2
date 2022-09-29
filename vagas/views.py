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

class MinhasVagasListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Vaga
    template_name = 'vagas/template/vagas/minhasvagas.html'

    def get_queryset(self):
        self.object_list = Vaga.objects.filter(usuario=self.request.user)
        return self.object_list

