from django.shortcuts import render
from .models import Vaga
from .forms import VagasForm
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

class VagaCreateView(LoginRequiredMixin, CreateView):
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

class VagaUpdateView(LoginRequiredMixin,UpdateView):
    login_url=reverse_lazy('login')
    form_class=VagasForm
    template_name='vagas/form.html'
    success_url=reverse_lazy('index')
    vagas_obj=Vaga.objects.all()

    def get_object(self, queryset: None):
        self.object=get_object_or_404(Vaga,pk=self.kwargs['pk'],usuario=self.user)
        return self.object

# def vaga_add(request):
#     if request.method=='POST':
#         form=VagasForm(request.POST)
#         if form.is_valid():
#             nova_vaga=form.save()
#             nova_vaga.save()
#             return HttpResponseRedirect('/vagas.html') # Nome provisório. A ser visto e alterado.
#     else:
#         form=VagasForm()

#     vagas=Vaga.objects.all()

#     return render(request,'vagas/add.html',
#     {
#         'form':form,
#         'vagas':vagas
#     }
#     )