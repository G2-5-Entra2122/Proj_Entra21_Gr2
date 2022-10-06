from django.urls import path
from .views import MinhasVagasListView, VagaCreateView,VagaUpdateView, MinhasVagasDeleteView

urlpatterns=[
    path('minhasvagas/adicionar/',VagaCreateView.as_view(),name='minhasvagas-adicionar'),

    path('minhasvagas/alterar/<int:pk>/',VagaUpdateView.as_view(), name='minhasvagas-alterar'),

    path('minhasvagas/',MinhasVagasListView.as_view(),name='minhas-vagas'),

    path('minhasvagas/deletar/<int:pk>/', MinhasVagasDeleteView.as_view(), name='minhasvagas-deletar')
]