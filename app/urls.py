from django.urls import path

from .views import HomeView, SobreView, VagasView, EmpresasView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('vagas', VagasView.as_view(), name='vagas'),
    path('empresas', EmpresasView.as_view(), name='empresas'),
    path('sobre_nos', SobreView.as_view(), name= 'sobre')
]