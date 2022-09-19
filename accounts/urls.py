from django.urls import path
from django.contrib.auth import views as auth_views
from .views import CandidatoCreate, EmpresaCreate, PerfilCandidatoUpdateView

urlpatterns = [
    # path('register/', views.SignUp.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(
            template_name='registration/login.html'
        ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registrar/candidato', CandidatoCreate.as_view(), name='registrar-candidato'),
    path('registrar/empresa', EmpresaCreate.as_view(), name='registrar-empresa'),
    path('atualizar-dados/', PerfilCandidatoUpdateView.as_view(), name='atualizar-dados'),

]
