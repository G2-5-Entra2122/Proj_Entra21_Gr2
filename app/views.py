from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'index.html'

class VagasView(TemplateView):
    template_name = 'vagas.html'

class EmpresasView(TemplateView):
    template_name = 'empresas.html'

class SobreView(TemplateView):
    template_name = 'about.html'


