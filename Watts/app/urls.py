from django.urls import path
from .views import HomeViews, AddLocacao, CriarComodo, CriarPontodeenergia

app_name = 'app'

urlpatterns = [
    path('', HomeViews.as_view(), name='home'),
    path('addLocacao/', AddLocacao.as_view(), name='addLocacao'),
    path('addComodo/', CriarComodo, name='addComodo'),
    path('addPontodeenergia/', CriarPontodeenergia.as_view(), name='addPontodeenergia'),
]
