from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CandidatoForm, HabilidadesForm
from django.http import HttpResponseRedirect
from .models import Candidato, Habilidades
from django.contrib import messages

from django.forms import formset_factory

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
    CandidatoFormSet = formset_factory(CandidatoForm)
    HabilidadesFormSet = formset_factory(HabilidadesForm)

    if request.method == 'POST':
        candidato_formset = CandidatoFormSet(request.POST, prefix='candidato')
        habilidades_formset = HabilidadesFormSet(request.POST, prefix='habilidades')
        if candidato_formset.is_valid() and habilidades_formset.is_valid():
            print()
            print(candidato_formset.cleaned_data)
            candidato_formset.cleaned_data
            print()
            habilidades_formset.cleaned_data
            print(habilidades_formset.cleaned_data)
            print()
            habilidade = Habilidades.objects.create(**habilidades_formset.cleaned_data[0])
            candidato = Candidato.objects.create(**candidato_formset.cleaned_data[0])
            candidato.habilidades.add(habilidade)
            candidato.save()
            return HttpResponseRedirect('thanks') 
    else:
        candidato_formset = CandidatoFormSet(prefix='candidato')
        habilidades_formset = HabilidadesFormSet(prefix='habilidades')
    
    context = {
        'candidato_formset': candidato_formset,
        'habilidades_formset': habilidades_formset
    }
    return render(request, 'candidato.html', context)

    # if request.method == 'POST':
    #     form = CandidatoForm(request.POST)
    #     if form.is_valid():
    #         form_instance = form.save(commit=False)
    #         # form = CandidatoForm()
    #         form2 = HabilidadesForm(request.POST, instance=form_instance)
    #         if form2.is_valid():
    #             form_instance.save()
    #             form2.save()
    #             return HttpResponseRedirect('thanks')
    #     else:
    #         messages.error(request, 'Erro ao cadastrar o candidato')
    # else:
    #     form = CandidatoForm()
    #     form2 = HabilidadesForm()
    
    # candidato = Candidato.objects.all()
    # habilidades = Habilidades.objects.all()

    # context = {
    #     'form': form,
    #     'candidato': candidato,
    #     'form2': form2,
    #     'habilidades': habilidades
    # }

    # return render(request, 'candidato.html', context)


@login_required
def thanks(request):
    mensagem = "Obrigado!"
    return render(request, 'thanks.html', {'mensagem': mensagem})