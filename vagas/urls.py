from django.urls import path
from .views import VagaCreateView,VagaUpdateView, VagaListView


urlpatterns=[
    path('minhasvagas/adicionar',VagaCreateView.as_view(),name='minhasvagas-adicionar'),
    path('lista/vagas', VagaListView.as_view(), name='vaga-list')
]

