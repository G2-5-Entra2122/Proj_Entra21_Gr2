from django.shortcuts import render
from models import Vaga
from forms import VagasForm
from django.http import HttpResponseRedirect

# login required a ser observado na review
def vaga_add(request):
    if request.method=='POST':
        form=VagasForm(request.POST)
        if form.is_valid():
            nova_vaga=form.save()
            nova_vaga.save()
            return HttpResponseRedirect('/vagas.html') # Nome provisório. A ser visto e alterado.
    else:
        form=VagasForm()

    vagas=Vaga.objects.all()

    return render(request,'vagas/add.html',
    {
        'form':form,
        'vagas':vagas
    }
    )