from django.urls import path
from .views import VagaCreateView,VagaUpdateView

urlpatterns=[
    path('minhasvagas/adicionar',VagaCreateView.as_view(),name='minhasvagas-adicionar'),
    path('minhasvagas/alterar',VagaUpdateView.as_view(), name='minhasvagas-alterar'),
    path('minhasvagas/'),

]