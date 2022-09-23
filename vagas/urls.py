from django.urls import path
from .views import VagaCreateView,VagaUpdateView

urlpatterns=[
    path('minhasvagas/adicionar',VagaCreateView.as_view(),name='minhasvagas-adicionar')
]