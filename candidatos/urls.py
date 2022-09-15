from django.urls import path

from .views import CandidatosCreateView, CurriculoCreateView, HabilidadesCreateView
from .views import CandidatosUpdateView, CurriculosUpdateView, HabilidadesUpdateView

urlpatterns = [
    path('candidato/perfil/', CandidatosCreateView.as_view(), name='candidato-perfil'),
    path('candidato/curriculo/', CurriculoCreateView.as_view(), name='candidato-curriculo'),
    path('candidato/habilidades/', HabilidadesCreateView.as_view(), name='candidato/habilidades'),

    path('editar/perfil/<int:pk>/', CandidatosUpdateView.as_view(), name='editar-perfil'),
    path('editar/perfil/<int:pk>/', CurriculosUpdateView.as_view(), name='editar-curriculo'),
    path('editar/perfil/<int:pk>/', HabilidadesUpdateView.as_view(), name='editar-habilidades'),
]