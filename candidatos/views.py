from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Curriculo
from .forms import CurriculoForm

from vagas.forms import FilterForm





################## UPDATEVIEW ##################



class CurriculosUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    form_class = CurriculoForm

    template_name = 'candidatos/form.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        # Define que apenas o usuario que criou o Form, pode editar-lo e se não for envia o usuario pra uma página 404.
        self.object = get_object_or_404(Curriculo, usuario=self.request.user)
        return self.object
        

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Meu curriculo'
        return context



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

class CandidatoListView(ListView):
    model = Curriculo
    template_name = 'candidatos/candidatos-list.html'
    paginate_by = 4

    def get_queryset(self):
        candidatos = Curriculo.objects.all()
        search_001 = self.request.GET.get('src01')
        if search_001:
            if search_001 != "todas-as-categorias":
                candidatos = candidatos.filter(categoria=search_001)

        search_002 = self.request.GET.get('src02')
        if search_002:
            if search_002 != "todas-as-modalidades":
                candidatos = candidatos.filter(modalidade=search_002)

        search_003 = self.request.GET.get('src03')
        if search_003:
            if search_003 != "tipo-de-contrato":
                candidatos = candidatos.filter(contrato=search_003)

        
        self.contador = candidatos.count()

        return candidatos

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)    
        context['contador']  = self.contador 
        context['form'] = FilterForm(initial={
            'search': self.request.GET.get('search', ''),
            'filter_field': self.request.GET.get('filter_field', '')
        })
        return context

class CandidatoPerfilView(DetailView):
    model = Curriculo
    template_name = 'candidatos/candidatos-perfil.html'
    
    