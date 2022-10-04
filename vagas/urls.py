from django.urls import path
from .views import MinhasVagasListView, VagaCreateView,VagaUpdateView, MinhasVagasDeleteView

urlpatterns=[
    path('minhasvagas/adicionar',VagaCreateView.as_view(),name='minhasvagas-adicionar'),
    #path('minhasvagas/alterar',VagaUpdateView.as_view(), name='minhasvagas-alterar'),=>adicionar o id 
    path('minhasvagas/',MinhasVagasListView.as_view(),name='minhas-vagas'),
    path('<pk>/minhasvagas/deletar', MinhasVagasDeleteView.as_view(), name='minhasvagas-deletar')
]