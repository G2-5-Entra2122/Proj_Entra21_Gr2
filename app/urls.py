from django.urls import path

from .views import HomeView, SobreView, EmpresasView, ErrorView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('empresas-lista', EmpresasView.as_view(), name='empresas'),
    path('about', SobreView.as_view(), name= 'about'),
    path('404', ErrorView.as_view(), name= '404'),
]