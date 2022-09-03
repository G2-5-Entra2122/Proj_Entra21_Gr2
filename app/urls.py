from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('vagas', views.vagas),
    path('empresas', views.empresas),
    path('candidato', views.candidato),
    path('thanks', views.thanks)
]