from django.urls import path
from balanca.views import listar_pesos

urlpatterns = [
    path('pesos/', listar_pesos, name='listar_pesos'),
]