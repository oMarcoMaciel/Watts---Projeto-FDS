from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.HomeViews.as_view(), name ='home'),
    path('addLocacao/', views.AddLocacao.as_view(), name = 'addLocacao'),
    path('addComodo/', views.CriarComodo, name = 'addComodo'),
]
