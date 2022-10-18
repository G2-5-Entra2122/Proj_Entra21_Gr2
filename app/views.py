from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'index.html'


class EmpresasView(TemplateView):
    template_name = 'empresas-lista.html'

class SobreView(TemplateView):
    template_name = 'about.html'

class ErrorView(TemplateView):
    template_name = '404.html'

class TabeladePrecosView(TemplateView):
    template_name = 'tabela-de-precos.html'
