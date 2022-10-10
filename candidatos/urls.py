from django.urls import path


from .views import CurriculosUpdateView
#from .views import CandidatoListView, CurrucloListView

urlpatterns = [

    path('atualizar-curriculo/', CurriculosUpdateView.as_view(), name='atualizar-curriculo'),

    # path('listar/perfil/', CandidatoListView.as_view(), name='listar-perfil'),
    # path('listar/curriculo', CurrucloListView.as_view(), name='listar-curriculo'),
]