from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.shortcuts import get_object_or_404

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


from .models import Curriculo
from .forms import CurriculoForm







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

class CandidatoPerfilView(DetailView):
    model = Curriculo
    template_name = 'candidatos/candidatos-perfil.html'