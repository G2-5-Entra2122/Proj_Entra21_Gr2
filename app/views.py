from django.shortcuts import render
from django.contrib.auth.decorators import login_required


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