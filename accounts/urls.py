from django.urls import path
from django.contrib.auth import views as auth_views
from .views import CandidatoCreate, EmpresaCreate, PerfilEmpresaUpdateView, PerfilCandidatoUpdateView, change_password
from accounts import views

urlpatterns = [
    # path('register/', views.SignUp.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(
            template_name='registration/login.html'
        ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registrar/candidato', CandidatoCreate.as_view(), name='registrar-candidato'),
    path('registrar/empresa', EmpresaCreate.as_view(), name='registrar-empresa'),
    path('atualizar-dados/candidato/', PerfilCandidatoUpdateView.as_view(), name='atualizar-dados'),
    path('atualizar-dados/empresa/', PerfilEmpresaUpdateView.as_view(), name='atualizar-dados-empresas'),
    path('alterar-senha', views.change_password, name='change-password') 

]
