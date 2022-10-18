from django.urls import path

from .views import MinhasVagasListView, VagaCreateView, VagaUpdateView, MinhasVagasDeleteView, VagaListView, VagaExibirListView

urlpatterns=[
    path('vagas/postar-vaga/',VagaCreateView.as_view(),name='vagas/postar-vaga'),

    path('minhasvagas/alterar/<int:pk>/',VagaUpdateView.as_view(), name='minhasvagas-alterar'),

    path('minhasvagas/',MinhasVagasListView.as_view(),name='minhas-vagas'),
    path('vagas/', VagaListView.as_view(), name='vaga-list'),

    path('minhasvagas/deletar/<int:pk>/', MinhasVagasDeleteView.as_view(), name='minhasvagas-deletar'),
    path('vagas/exibirvaga/<int:pk>/', VagaExibirListView.as_view(), name='exibirvaga'),
]
