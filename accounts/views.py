from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import Group
from .forms import CandidatoForm, EmpresaForm, PerfilEmpresasForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required


from .models import PerfilEmpresas
from candidatos.models import Curriculo

class EmpresaCreate(CreateView):
    template_name = 'registration/register.html'
    form_class = EmpresaForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):

        grupo = get_object_or_404(Group, name="Empresa")
        
        url = super().form_valid(form)
        
        self.object.groups.add(grupo)
        self.object.save()

        PerfilEmpresas.objects.create(usuario=self.object)

        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Registro da empresa'
        return context

class CandidatoCreate(CreateView):
    template_name = 'registration/register.html'
    form_class = CandidatoForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):

        grupo = get_object_or_404(Group, name="Candidato")
        
        url = super().form_valid(form)
        
        self.object.groups.add(grupo)
        self.object.save()

        CandidatoForm.objects.create(usuario=self.object)

        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Registro do candidato'
        return context


class PerfilEmpresaUpdateView(UpdateView):
    form_class = PerfilEmpresasForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        # Define que apenas o usuario que criou o Form, pode editar-lo e se não for envia o usuario pra uma página 404.
        self.object = get_object_or_404(PerfilEmpresas, usuario=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Dados da empresa'
        return context


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            messages.success(request, 'Você alterou sua senha com sucesso!')
            return redirect ('index')
        else:
            messages.error(request, 'Tente novamente!')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/changepassword.html', {
        'form' : form
    })