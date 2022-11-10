from django.views.generic import TemplateView
from django.views.generic import ListView
from accounts.models import PerfilEmpresas


class HomeView(TemplateView):
    template_name = 'index.html'
    model = PerfilEmpresas
        
    def contador(self):
        count = PerfilEmpresas.objects.all().count()
        return count
    


class EmpresasView(TemplateView):
    template_name = 'empresas-lista.html'

class SobreView(TemplateView):
    template_name = 'about.html'

class ErrorView(TemplateView):
    template_name = '404.html'

class TabeladePrecosView(TemplateView):
    template_name = 'tabela-de-precos.html'

class FaqView(TemplateView):
    template_name = 'faq.html'

class TabeladePrecosView(TemplateView):
    template_name = 'tabela-de-precos.html'
