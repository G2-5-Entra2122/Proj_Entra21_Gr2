from django.urls import path

from .views import CandidatosCreateView, CurriculoCreateView, HabilidadesCreateView

urlpatterns = [
    path('candidato/perfil/', CandidatosCreateView.as_view(), name='candidato-perfil'),
    path('candidato/curriculo/', CurriculoCreateView.as_view(), name='candidato-curriculo'),
    path('candidato/habilidades/', HabilidadesCreateView.as_view(), name='candidato/habilidades'),
]