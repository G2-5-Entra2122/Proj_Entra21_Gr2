from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CandidatoForm
from django.http import HttpResponseRedirect
from .models import Candidato
from django.contrib import messages


@login_required
def home(request):

    data = "Versao 0.01"

    return render(request, 'index.html', 
        { 'dados' : data } 
    )

@login_required
def vagas(request):

    data = "Versao 0.01 - Dashboard 1 (um) "

    return render(request, 'vagas.html', 
        { 'dados' : data } 
    )    

@login_required
def empresas(request):

    data = "Versao 0.01 - Dashboard 2 (dois)"

    return render(request, 'empresas.html', 
        { 'dados' : data } 
    )

@login_required
def candidato(request):

    if request.method == 'POST':
        form = CandidatoForm(request.POST)
        if form.is_valid():
            form.save()
            form = CandidatoForm()
            return HttpResponseRedirect('thanks')
        else:
            messages.error(request, 'Erro ao cadastrar o candidato')
    else:
        form = CandidatoForm()
    
    candidato = Candidato.objects.all()

    context = {
        'form': form,
        'candidato': candidato
    }

    return render(request, 'candidato.html', context)


@login_required
def thanks(request):
    mensagem = "Obrigado!"
    return render(request, 'thanks.html', {'mensagem': mensagem})