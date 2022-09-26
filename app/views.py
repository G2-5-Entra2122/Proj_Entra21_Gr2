# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from .forms import CandidatoForm, HabilidadesForm
# from django.http import HttpResponseRedirect
# from .models import Candidato, Habilidades
# from django.contrib import messages
# from django.forms import formset_factory
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'index.html'

class VagasView(TemplateView):
    template_name = 'vagas.html'

class EmpresasView(TemplateView):
    template_name = 'empresas.html'

class SobreView(TemplateView):
    template_name = 'sobre.html'


# @login_required
# def candidato(request):
#     CandidatoFormSet = formset_factory(CandidatoForm)
#     HabilidadesFormSet = formset_factory(HabilidadesForm)

#     if request.method == 'POST':
#         candidato_formset = CandidatoFormSet(request.POST, prefix='candidato')
#         habilidades_formset = HabilidadesFormSet(request.POST, prefix='habilidades')
#         if candidato_formset.is_valid() and habilidades_formset.is_valid():
#             print()
#             print(candidato_formset.cleaned_data)
#             candidato_formset.cleaned_data
#             print()
#             habilidades_formset.cleaned_data
#             print(habilidades_formset.cleaned_data)
#             print()
#             habilidade = Habilidades.objects.create(**habilidades_formset.cleaned_data[0])
#             candidato = Candidato.objects.create(**candidato_formset.cleaned_data[0])
#             candidato.habilidades.add(habilidade)
#             candidato.save()
#             return HttpResponseRedirect('thanks') 
#     else:
#         candidato_formset = CandidatoFormSet(prefix='candidato')
#         habilidades_formset = HabilidadesFormSet(prefix='habilidades')
    
#     context = {
#         'candidato_formset': candidato_formset,
#         'habilidades_formset': habilidades_formset
#     }
#     return render(request, 'candidato.html', context)



# @login_required
# def thanks(request):
#     mensagem = "Obrigado!"
#     return render(request, 'thanks.html', {'mensagem': mensagem})

