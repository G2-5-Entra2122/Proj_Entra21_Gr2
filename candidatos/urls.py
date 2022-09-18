from django.urls import path

from .views import CandidatosCreateView, CurriculoCreateView, HabilidadesCreateView
from .views import CandidatosUpdateView, CurriculosUpdateView, HabilidadesUpdateView
#from .views import CandidatoListView, CurrucloListView

urlpatterns = [
    path('candidato/perfil/', CandidatosCreateView.as_view(), name='candidato-perfil'),
    path('candidato/curriculo/', CurriculoCreateView.as_view(), name='candidato-curriculo'),
    path('candidato/habilidades/', HabilidadesCreateView.as_view(), name='candidato/habilidades'),

    path('editar/perfil/<int:pk>/', CandidatosUpdateView.as_view(), name='editar-perfil'),
    path('editar/curriculo/<int:pk>/', CurriculosUpdateView.as_view(), name='editar-curriculo'),
    path('editar/habilidades/<int:pk>/', HabilidadesUpdateView.as_view(), name='editar-habilidades'),

    # path('listar/perfil/', CandidatoListView.as_view(), name='listar-perfil'),
    # path('listar/curriculo', CurrucloListView.as_view(), name='listar-curriculo'),
]