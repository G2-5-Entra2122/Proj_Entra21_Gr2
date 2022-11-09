from django.urls import path
from django.contrib.auth import views as auth_views
from .views import EmpresaCreate, PerfilEmpresaUpdateView, change_password
from accounts import views
from .forms import LoginForm

urlpatterns = [
    # path('register/', views.SignUp.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(
            template_name='registration/login.html', authentication_form=LoginForm
        ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registrar/empresa', EmpresaCreate.as_view(), name='registrar-empresa'),
    path('atualizar-dados/empresa/', PerfilEmpresaUpdateView.as_view(), name='atualizar-dados-empresas'),

    path('alterar-senha', views.change_password, name='change-password') 

]
