from django.urls import path

from .views import HomeView, SobreView, EmpresasView, ErrorView, TabeladePrecosView, FaqView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('empresas-lista', EmpresasView.as_view(), name='empresas'),
    path('about', SobreView.as_view(), name= 'about'),
    path('about', ErrorView.as_view(), name= '404'),
    path('tabela-de-precos', TabeladePrecosView.as_view(), name= 'tabela-de-precos'),
]