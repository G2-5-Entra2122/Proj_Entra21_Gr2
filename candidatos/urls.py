from django.urls import path

# from .views import CurriculoCreateView, HabilidadesCreateView
from .views import CurriculosUpdateView, HabilidadesUpdateView
#from .views import CandidatoListView, CurrucloListView

urlpatterns = [

    #path('candidato/curriculo/', CurriculoCreateView.as_view(), name='candidato-curriculo'),
    #path('candidato/habilidades/', HabilidadesCreateView.as_view(), name='candidato/habilidades'),

    path('atualizar-curriculo/', CurriculosUpdateView.as_view(), name='atualizar-curriculo'),
    path('atualizar/habilidades/<int:pk>/', HabilidadesUpdateView.as_view(), name='atualizar-habilidades'),

    # path('listar/perfil/', CandidatoListView.as_view(), name='listar-perfil'),
    # path('listar/curriculo', CurrucloListView.as_view(), name='listar-curriculo'),
]