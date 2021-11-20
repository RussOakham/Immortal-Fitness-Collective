""" required imports for module functionality """
from django.apps import AppConfig


class ProductsConfig(AppConfig):
    """ Configure Products App """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'

    def ready(self):
        import products.signals
