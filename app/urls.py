from django.urls import path

from .views import HomeView, SobreView, EmpresasView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('empresas', EmpresasView.as_view(), name='empresas'),
    path('about', SobreView.as_view(), name= 'about')
]