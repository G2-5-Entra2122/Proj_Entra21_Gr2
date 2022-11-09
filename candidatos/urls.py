from django.urls import path


from .views import CurriculosUpdateView
from .views import CandidatoPerfilView, CandidatoListView, CandidatoDescricaoView

urlpatterns = [

    path('atualizar-curriculo/', CurriculosUpdateView.as_view(), name='atualizar-curriculo'),

    path('candidatos/', CandidatoListView.as_view(), name='candidatos-list'),
    # path('listar/curriculo', CurriculoListView.as_view(), name='listar-curriculo'),
    path('candidatos/perfil/<int:pk>', CandidatoPerfilView.as_view(), name='candidato-perfil'),
]