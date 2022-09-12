from django.urls import path

from .views import HomeView, VagasView, EmpresasView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('vagas', VagasView.as_view(), name='vagas'),
    path('empresas', EmpresasView.as_view(), name='empresas')
]