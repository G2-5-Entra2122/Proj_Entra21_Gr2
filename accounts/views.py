from django.views.generic.edit import CreateView
from .forms import CandidatoForm, EmpresaForm
from django.urls import reverse_lazy


class CandidatoCreate(CreateView):
    template_name = 'registration/register.html'
    form_class = CandidatoForm
    success_url = reverse_lazy('login')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Registro do candidato'
        return context


class EmpresaCreate(CreateView):
    template_name = 'registration/register.html'
    form_class = EmpresaForm
    success_url = reverse_lazy('login')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Registro da empresa'
        return context