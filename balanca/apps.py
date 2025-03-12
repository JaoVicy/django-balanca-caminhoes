from django.apps import AppConfig


class BalancaConfig(AppConfig):
    name = 'balanca'

    def ready(self):
        from .views import listar_pesos
