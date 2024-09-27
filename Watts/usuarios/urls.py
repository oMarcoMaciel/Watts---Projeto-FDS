from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('', views.HomeViews.as_view(), name ='home'),
    path('cadastro/', views.CadastroView, name = 'cadastro'),
    path('login/', views.LoginView, name = 'login'),
]
