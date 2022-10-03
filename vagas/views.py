from .models import Vaga
from .forms import VagasForm
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect


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
    
    def get_object(self, queryset: None):
        self.object=get_object_or_404(Vaga,pk=self.kwargs['pk'],usuario=self.user)
        return self.object

class MinhasVagasListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = u'Empresa'
    model = VagasForm
    template_name = 'vagas/minhasvagas.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs )

        context['titulo'] = 'Minhas Vagas'
        return context

    def get_queryset(self):
        self.object_list = Vaga.objects.filter(usuario=self.request.user)
        return self.object_list
        

class MinhasVagasDeleteView(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
   group_required = u'Empresas'
   model = Vaga
   success_url ="/"
   template_name ='vagas/deletevagas.html'

   def delete_view(request, id):
    context ={}
 
    obj = get_object_or_404(Vaga, id = id)
 
 
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/")
 
    return render(request, "delete_view.html", context)
