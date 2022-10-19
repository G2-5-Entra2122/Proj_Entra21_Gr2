from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.shortcuts import get_object_or_404
# from django.views.generic.list import ListView
from .models import Curriculo







################## UPDATEVIEW ##################



class CurriculosUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Curriculo
    fields = [
        'categoria',
        'nivel', 
        'contrato', 
        'modalidade',
        'salario',
        'pri_habilidade_candidato',
        'seg_habilidade_candidato',
        'ter_habilidade_candidato',
        'qua_habilidade_candidato',
        'qui_habilidade_candidato'
        ]
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